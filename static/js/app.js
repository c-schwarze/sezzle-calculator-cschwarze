$( document ).ready(function() {
    $("#submit").click(function() {
        $.ajax({
            type: "POST",
            data: $("#calculator").serialize(),
            url: "/calculate"
        });
    })

    setInterval(function(){
        $.ajax({
            type: "POST",
            url: "/get_output",
            success: function(data) {
                $("#output").html(data);
            }
        })
    }, 2000);
})