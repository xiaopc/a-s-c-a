# -*- coding: utf-8 -*-
import requests
import time
import random
import sys
import logging
import logging.handlers
from bs4 import BeautifulSoup


if (len(sys.argv)<=3) or (len(sys.argv)%3!=0) :
    exit()

user = sys.argv[1]
passwd = sys.argv[2]

paramcount = int(len(sys.argv)/3 - 1)
params = []
for num in range(1,paramcount+1):
    params.append({'kch': sys.argv[3*num], 'cxkxh': sys.argv[3*num+1], 'name': sys.argv[3*num+2]})

requestTimeoutLimit = 1    #单次连接超时，连接速度慢可适当加大
tryTimeout = 10            #每两次间隔时间

print(params)

cookies = {'JSESSIONID':'acbjrbXdfmdoSb9xX'+str(random.randint(0000, 9999))}
count = 0
error = 0
session = requests.Session()
printword = [
        "第%2d次请求 课程号 %s(%s)",
        "第%2d次异常 %s",
        "      状态 %s",
        "选课成功",
        "选课完成",
        "未知错误",
        "手动退出",
        "正在登录",
            ]
findtext = [
        "你已经选择了",
        "错误信息",
        "请您登录后再使用",
	    "<font color"
            ]
# LOG_FILE='logs/'+user+'.txt'
handler=logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
fmt = '%(asctime)s - %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger = logging.getLogger('asca')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def login():
    logger.info(printword[7])
    data = {'zjh': user, 'mm': passwd}
    #s = session.post("loginAction.do",data=data,cookies=cookies,timeout=requestTimeoutLimit)
    #s = session.get('xkAction.do?actionType=-1',cookies=cookies,timeout=requestTimeoutLimit)
    #s = session.get("xkAction.do?actionType=5&pageNumber=-3",cookies=cookies,timeout=requestTimeoutLimit)

def autopost():
    global count
    global params

    while True:
        for x in params:
            count = count+1
            logger.info(printword[0] %(count,x['kch'],x['name']))

            kcId = x['kch']+ '_' + x['cxkxh']
            x.setdefault('actionType','5')
            x.setdefault('preActionType','2')
            x.setdefault('kcm','')
            x.setdefault('skjs','')
            x.setdefault('kkxsjc','')
            x.setdefault('skxq', '')
            x.setdefault('skjc', '')
            x.setdefault('pageNumber','-2')
            #s = session.post("xkAction.do",params=x,cookies=cookies,timeout=requestTimeoutLimit)
            data2 = {'kcId':kcId,'preActionType':'5','actionType':'9'}
            #s = session.post('xkAction.do',params=data2,cookies=cookies,timeout=requestTimeoutLimit)

            if findtext[0] in s.text:
                params.remove(x)
                logger.info(printword[3])
            else:
                if findtext[1] in s.text or findtext[3] in s.text:
                    soup = BeautifulSoup(s.text, "html.parser")
                    logger.info(soup.font.get_text())
                    if findtext[2] in s.text:
                        login()
                else:
                    logger.info(printword[5])
                time.sleep(tryTimeout)

        if not params:
            break
# ----------------------------------------------


try:
    login()
    autopost()
    logger.info(printword[4])
except KeyboardInterrupt:
    logger.info(printword[6])
    sys.exit(1)
except ValueError:
    raise
except BaseException as argument:
    error = error + 1
    logger.info(printword[1] %(error, argument))
finally:
    autopost()
