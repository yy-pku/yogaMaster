window.onload = function () {
    var data={};
    data["usrid"]= 2;
    console.log(data);
	 $.ajax({
	 	url:"/usr/getFavorites",
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
                html+='<div class="ui card"><div class="eight wide tablet four wide computer column"><div class="ui fluid image">'+
                      '<svg width="150" height="120"><image  xlink:href="'+imgdata[i]+'" x="0" y="0" width="200%" height="200%"></image>'+
                      '</svg></div></div><div class="extra content">'+
                      '<div class="ui left labeled button" tabindex="0"><a class="ui basic right pointing label">100</a><div class="ui button">'+
                      '<i class="star icon active yellow"></i> Favorite</div></div></div></div>'
            }
            document.getElementById("imgbox").innerHTML=html;
	 	},
	 	error:function(e){
	 		alert("获取失败！请重试！");
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
	 		alert("获取失败！请重试！");
	 	}
	 });
}

function nextuser(){
    window.location.href="/static/usrFav.html";
}