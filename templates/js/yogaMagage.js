window.onload = function () {
	 $.ajax({
	 	url:"/home/getAllYoga",
	 	type:"GET",
	 	dataType: 'json',
	 	success:function(response){
	 		console.log(response);
	 		var imgdata=eval(response.data);
	 		var html="";
            for(var i=0,len=imgdata.length;i<len;i++)
            {
                var imgpath=imgdata[i]['image'];
                html+='<div class="eight wide tablet four wide computer column">'+
                                                            '<div class="ui segments">'+
                                                                '<div class="ui segment">'+
                                                                    '<h5 class="ui header">'+imgdata[i]['yogaName']+
                                                                    '</h5></div>'+
                                                                '<div class="ui segment"><div class="ui fluid image">'+
                                                                        '<svg width="150" height="120"><image  xlink:href="'+
                                                                        imgpath+
                                                                        '" x="0" y="0" width="100%" height="100%"></image>'+
                                                                        '</svg></div></div></div></div>';
            }
            document.getElementById("imgbox").innerHTML=html;
	 	},
	 	error:function(e){
	 		alert("获取失败！请重试！");
	 	}
	 });

	
}

function getYogaList(level){
    var data={};
    data["level"]=level;
    console.log(data);
	 $.ajax({
	 	url:"/home/getYogaByLevel",
	 	type:"POST",
	 	data:JSON.stringify(data),
	 	dataType: "json",
	 	contentType:'application/json;charset=UTF-8',
	 	success:function(response){
	 		console.log(response);
	 		var imgdata=eval(response.data);
	 		var html="";
            for(var i=0,len=imgdata.length;i<len;i++)
            {
                var imgpath=imgdata[i]['image'];
                html+='<div class="eight wide tablet four wide computer column">'+
                                                            '<div class="ui segments">'+
                                                                '<div class="ui segment">'+
                                                                    '<h5 class="ui header">'+imgdata[i]['yogaName']+
                                                                    '</h5></div>'+
                                                                '<div class="ui segment"><div class="ui fluid image">'+
                                                                        '<svg width="150" height="120"><image  xlink:href="'+
                                                                        imgpath+
                                                                        '" x="0" y="0" width="100%" height="100%"></image>'+
                                                                        '</svg></div></div></div></div>';
            }
            document.getElementById("imgbox").innerHTML=html;
	 	},
	 	error:function(e){
	 		alert("获取失败！请重试！");
	 	}
	 });
}