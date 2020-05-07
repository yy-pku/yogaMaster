window.onload = function () {
    $.ajax({
	 	url:"/usr/getAllUsr",
	 	type:"GET",
	 	dataType: 'json',
	 	success:function(response){
	 		console.log(response);
	 		var usrdata=eval(response.data);
	 		var html="";
            for(var i=0,len=usrdata.length;i<len;i++)
            {
                html+='<tr onclick=toUsr('+usrdata[i]['usrid']+')><td>'+usrdata[i]['usrid']+'</td><td>'+usrdata[i]['nickname']+'</td><td>'+usrdata[i]['country']+'</td><td>'+
                    usrdata[i]['province']+'</td><td>'+usrdata[i]['city']+'</td><td>'+usrdata[i]['gender']+'</td><td>'+
                    usrdata[i]['lastLoginTime']+'</td></tr>';
            }
            document.getElementById("tablebox").innerHTML=html;
	 	},
	 	error:function(e){
	 		alert("获取失败！请重试！");
	 	}
	 });
}

function toUsr(usrid){
    var myurl="/static/usrFav.html"+"?"+"usrid="+usrid;
    window.location.assign(encodeURI(myurl));
}