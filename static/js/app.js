$( document ).ready(function() {
    calc_btn = $(".calc-btn")
    calc_btn.click(function() {
        // todo: need to add logic so you can't put multiple equations
        full_equation = $('#full-equation');
        full_equation.val(full_equation.val() + $(this).val());
    })


    $("#submit-btn").click(function() {
        $.ajax({
            type: "POST",
            data: $("#calculator").serialize(),
            url: "/calculate",
            success: function(data) {
                if( data != 'success')
                    alert(data);
            }
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