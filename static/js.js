errInfo=[]
errInfo["401"]="unauthorized";
errInfo["406"]="info not acceptable";
errInfo["423"]="id exists and was locked";


$(function(){ 

    $("#login-form").on("submit",function(e){
        $.post("socket.php?action=add&code="+$("#form-code").val(), { "id": $("#form-id").val(),
                               "pass": $("#form-pass").val(),
                               "kch1": $("#form-kch1").val(),
                               "kxh1": $("#form-kxh1").val(),
                               "note1": $("#form-note1").val(),
                               "kch2": $("#form-kch2").val(),
                               "kxh2": $("#form-kxh2").val(),
                               "note2": $("#form-note2").val(),
                               "kch3": $("#form-kch3").val(),
                               "kxh3": $("#form-kxh3").val(),
                               "note3": $("#form-note3").val(),
                             },
                function(data){
                    if (data.status!="200") {
                        var n = noty({
                        	text: 'error code:'+data.status+'('+errInfo[data.status]+')',
                        	layout: 'centerLeft',
                        	type: 'error',
                        	timeout: 5000,
                        	progressBar: true
                        });
                    } else {
                        var n = noty({
                        	text: 'successfully add '+data.data+' class(es) to task list. click here and it will redirect to status monitor page...',
                        	layout: 'centerLeft',
                        	type: 'success',
                        	callback: {afterClose: function() {
                            									window.location.href= 'socket.php?action=view&id='+$("#form-id").val();
                        									  }
                    				  }
                		});
                        
                    }
                }, "json");
           
        e.preventDefault();
    });

}); 