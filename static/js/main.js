$.ajaxSetup({
    beforeSend: function(){
        NProgress.start();
    },
    success: function(){
        NProgress.done();
    },
    complete: function(){
        NProgress.done();
    }
});

$("#irisForm").submit(function(event){
    event.preventDefault();
    $("#predictedClass").html("");
    $.ajax({
      url: "checkResults",
      cache: false,
      method: "POST",
      data:$("#irisForm").serialize(),
      success: function(data) {
        $("#predictedClass").html(data);
      }
    });
});