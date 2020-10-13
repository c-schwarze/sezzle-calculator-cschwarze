$( document ).ready(function() {
    $("#submit").click(function() {
        $.ajax({
            type: "POST",
            data: $("#calculator").serialize(),
            url: "/calculate"
//            success: function(data) {
//                console.log(data);
//            }
        });
    })
})