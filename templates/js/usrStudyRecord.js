var url=location.href; 
var tmp1="",temp2="",data={},usrid="";
console.log(url);
if(url.indexOf("?")!=-1){
    tmp1=url.split("?")[1];  
    tmp2=tmp1.split("=")[1]; 
    usrid=tmp2;
} else{
    usrid= 2;
}
data["usrid"]= usrid;
console.log(data);
window.onload = function () {
	 $.ajax({
	 	url:"/usr/getStudyRecord",
	 	type:"POST",
	 	dataType: 'json',
	 	data:JSON.stringify(data),
	 	contentType:'application/json;charset=UTF-8',
	 	success:function(response){
	 		console.log(response);
	 		var imgdata=eval(response.data);
	 		var html="";
            for(var i=0,len=imgdata.length;i<len;i++)
            {
                html+='<div class="card"><div class="eight wide tablet four wide computer column"><div class="ui segments">'+
                      '<div class="ui segment"><div class="ui fluid image"><svg width="150" height="120"><image  xlink:href="'+
                      imgdata[i]+'" x="0" y="0" width="200%" height="200%"></image></svg></div></div></div></div></div>';

            }
            document.getElementById("imgbox").innerHTML=html;
	 	},
	 	error:function(e){
	 		alert("没有下一个用户了！");
	 	}
	 });
    $.ajax({
	 	url:"/usr/getUsrInfo",
	 	type:"POST",
	 	dataType: 'json',
	 	data:JSON.stringify(data),
	 	contentType:'application/json;charset=UTF-8',
	 	success:function(response){
	 		console.log(response);
	 		var usrdata=eval(response.data);
	 		document.getElementById("avatar").src=usrdata[0]['avatarUrl'];
	 		var html="";
            html+='<div class="header"><i class="like icon"></i>'+usrdata[0]['nickname']
                   '</div><div class="meta">'+usrdata[0]['country']+'<i class="icon map marker"></i></div>';
            document.getElementById("usrbox").innerHTML=html;
	 	},
	 	error:function(e){
	 		alert("没有下一个用户了！");
	 	}
	 });


}

function nextuser(){
    usrid++;
    var myurl="/static/usrStudyRecord.html"+"?"+"usrid="+usrid;
    window.location.assign(encodeURI(myurl));
}

function toPage(){
    var myurl="/static/usrFav.html"+"?"+"usrid="+usrid;
    window.location.assign(encodeURI(myurl));
}