$(document).ready(function() {
    $('.follow-button').click(function() {
        var userId = $(this).data('id');
        var url = '/follow/' + userId + '/';
        var button = $(this);

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response) {
                if (response.following) {
                    button.html('Unfollow');
                    $('#followers-count').html(response.followers_count);
                } else {
                    button.html('Follow');
                    $('#followers-count').html(response.followers_count);
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});