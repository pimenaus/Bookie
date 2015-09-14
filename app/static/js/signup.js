/**
 * Created by Alexey on 03.09.2015.
 */
$(function() {
    $('#btnSignUp').click(function() {

        $.ajax({
            url: '/onRegister',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
