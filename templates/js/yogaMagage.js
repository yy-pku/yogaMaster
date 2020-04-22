window.onload = function () {
	// var imgdata;
	// $.ajax({
	// 	url:"/home/getAllYoga",
	// 	type:"GET",
	// 	success:function(response){
	// 		console.log(response);
	// 		imgdata=response.data;
	// 	},
	// 	error:function(e){
	// 		alert("获取失败！请重试！");
	// 	}
	// });
	
	var imgdata=[
		        {imageName:1,image:"img/yoga/primary/buttocks.jpg"},
				{imageName:2,image:"img/yoga/primary/buttocks.jpg"},
				{imageName:3,image:"img/yoga/primary/buttocks.jpg"},
				{imageName:4,image:"img/yoga/primary/buttocks.jpg"},
				{imageName:5,image:"img/yoga/primary/buttocks.jpg"},
	        ];
	var html="";
	for(var i=0,len=imgdata.length;i<len;i++)
	{
		html+='<div class="eight wide tablet four wide computer column">'+
		                                            '<div class="ui segments">'+
		                                                '<div class="ui segment">'+
		                                                    '<h5 class="ui header">'+imgdata[i]['imageName']+
		                                                    '</h5></div>'+
		                                                '<div class="ui segment"><div class="ui fluid image">'+
		                                                        '<svg width="150" height="120"><image  xlink:href="'+
																imgdata[i]['image']+
																'" x="0" y="0" width="100%" height="100%"></image>'+
		                                                        '</svg></div></div></div></div>';
	}
	document.getElementById("imgbox").innerHTML=html;
	
}

function getYogaList(level){
	// var imgdata;
	// var params={
 //        level: level
 //    };
	// $.ajax({
	// 	url:"/home/getYogaList",
	// 	type:"GET",
	// 	data:params,
	// 	dataType: "json",
	// 	success:function(response){
	// 		console.log(response);
	// 		imgdata=response.data;
	// 	},
	// 	error:function(e){
	// 		alert("获取失败！请重试！");
	// 	}
	// });
	var imgdata=[
		        {imageName:1,image:"img/yoga/primary/buttocks.jpg"},
				{imageName:2,image:"img/yoga/primary/buttocks.jpg"},
				{imageName:3,image:"img/yoga/primary/buttocks.jpg"},
				{imageName:4,image:"img/yoga/primary/buttocks.jpg"},
				{imageName:5,image:"img/yoga/primary/buttocks.jpg"},
	        ];
	var html="";
	for(var i=0,len=imgdata.length;i<len;i++)
	{
		html+='<div class="eight wide tablet four wide computer column">'+
		                                            '<div class="ui segments">'+
		                                                '<div class="ui segment">'+
		                                                    '<h5 class="ui header">'+imgdata[i]['imageName']+
		                                                    '</h5></div>'+
		                                                '<div class="ui segment"><div class="ui fluid image">'+
		                                                        '<svg width="150" height="120"><image  xlink:href="'+
																imgdata[i]['image']+
																'" x="0" y="0" width="100%" height="100%"></image>'+
		                                                        '</svg></div></div></div></div>';
	}
	document.getElementById("imgbox").innerHTML=html;
}