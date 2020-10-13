$( document ).ready(function() {
    // replace enter key with submitting equation
    $(document).on('keypress',function(e) {
        if(e.which == 13) {
            submit_equation();
            event.preventDefault();
        }
    });

    // add the new value to the field
    calc_btn = $(".calc-btn")
    calc_btn.click(function() {
        // todo: need to add logic so you can't put multiple equations
        full_equation = $('#full-equation').val();
        new_input = $(this).val();

        // you must start with a number, otherwise the equation doesn't make sense.
        if(full_equation == '' && !$.isNumeric(new_input) ) {
            return;
        }

        // if a new operator is entered and the last was an operator, replace with new operator
        // todo: this could be improved by using regex.
        if(!$.isNumeric(new_input) && ['+', '-', '*', '/'].includes(full_equation.charAt(full_equation.length - 2))){
            full_equation = full_equation.slice(0, -3);
        }

        // add value to the full equation
        $('#full-equation').val(full_equation + new_input);
    })


    // on equals button press, submit equation
    $("#equals-btn").click(function() {
        submit_equation();
    })

    // submit the equation for processing
    function submit_equation(){
        $.ajax({
            type: "POST",
            data: $("#calculator").serialize(),
            url: "/calculate",
            success: function(data) {
                if( data != 'success')
                    alert(data);
                else
                    $('#full-equation').val('')
            }
        });
    }

    // every 1 second, pull new data
    setInterval(function(){
        $.ajax({
            type: "POST",
            url: "/get_output",
            success: function(data) {
                $("#output").html(data);
            }
        })
    // updated every 1 second
    }, 1000);
})