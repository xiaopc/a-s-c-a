<?php
if (!defined('TESTED')){die();}

if ( empty($result[id]) || empty($result[pass]) || (int)($result[id])<2010000000000 || (int)($result[id])>2099000000000 ) {
    die('{"status":"406"}');
}

$filename = "./confs/sk".$result[id].".conf";
if (file_exists($filename)){ die('{"status":"423"}'); }

$word = '[program: sk'.$result[id].']
directory = /home/wwwroot/tj1.xpc.im/xkaction
command = /usr/bin/python3 server.py "'.$result[id].'" "'.$result[pass].'" ';

$counter=0;
if ( !empty($result[kch1]) && !empty($result[kxh1]) && !empty($result[note1]) ) {
    $word = $word.'"'.$result[kch1].'" "'.$result[kxh1].'" "'.$result[note1].'" ';
    $counter++;
}
if ( !empty($result[kch2]) && !empty($result[kxh2]) && !empty($result[note2])) {
    $word = $word.'"'.$result[kch2].'" "'.$result[kxh2].'" "'.$result[note2].'" ';
    $counter++;
}
if ( !empty($result[kch3]) && !empty($result[kxh3]) && !empty($result[note3])) {
    $word = $word.'"'.$result[kch3].'" "'.$result[kxh3].'" "'.$result[note3].'" ';
    $counter++;
}
$word = $word."\n";

$fh = fopen($filename, "w");
fwrite($fh, $word);
fclose($fh);

$r1 = exec("/usr/bin/supervisorctl reread");
$r2 = exec('/usr/bin/supervisorctl update');

echo '{"status":"200","data":"'.$counter.'","info":"'.$r1.$r2.'"}';

?>
