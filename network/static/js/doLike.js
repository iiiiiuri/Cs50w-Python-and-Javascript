$('.like-div').click(function() {
    var postId = $(this).data('id');
    var url = '/do_like/' + postId + '/';
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'csrfmiddlewaretoken': csrftoken
        },
        success: function(response) {
            if (response.liked) {
                $('#like-icon-' + postId).removeClass('bi-heart').addClass('bi-heart-fill');
                $('#like-count-' + postId).text(response.like_count);
                $('#like-text-' + postId).text('Unlike');
            } else {
                $('#like-icon-' + postId).removeClass('bi-heart-fill').addClass('bi-heart');
                $('#like-count-' + postId).text(response.like_count);
                $('#like-text-' + postId).text('Like');
            }
        }
    });
});