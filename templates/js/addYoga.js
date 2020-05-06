function addYoga(){
        var formData=new FormData();//
		formData.append("yogaName",document.getElementById("yoganame").value);
		var options=$("#level option:selected");
		formData.append("level",options.val());
		formData.append("imgDescription",document.getElementById("imgdescription").value);
		formData.append("yogaImg",$('#image')[0].files[0]);
		console.log(formData);
        $.ajax({
            url:"/home/addYoga",
            type:"POST",
            data:formData,
            processData: false,
            contentType: false,
            success:function(response){
                alert("成功添加瑜伽姿势信息！");
            },
            error:function(e){
                alert("添加失败！请重新添加！");
            }
        });

}