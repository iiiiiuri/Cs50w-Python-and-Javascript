$(document).ready(function() {
    $('.edit_post').click(function(e) {
        e.preventDefault();
        var postId = $(this).data('id');
        var url = '/edit_post/' + postId + '/';

        var formData = new FormData();
        formData.append('content', $('#edit-form textarea[name="content"]').val());
        var fileInput = $('.file-input')[0];
        if (fileInput.files.length > 0) {
            formData.append('image', fileInput.files[0]);
        }

        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            processData: false,
            contentType: false,
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                $('#edit-form textarea[name="content"]').val(response.content);
                $('#edit-form').attr('action', '/edit_post/' + postId + '/');
                $('#edit-modal').removeClass('hidden');
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('#edit-form textarea[name="content"]').on('input', function() {
        $('#save-button').removeClass('hidden');
    });

    $('#save-button').click(function(e) {
        e.preventDefault();
        $('#edit-form').submit();
    });

    $('#cancel-button').click(function(e) {
        e.preventDefault();
        $('#edit-modal').addClass('hidden');
    });

    $('.file-upload').click(function(e) {
        $(this).find('.file-input').click();
    });

    $('.file-input').click(function(e) {
        e.stopPropagation();
    });

    $('.file-input').change(function(e) {
        var fileName = e.target.files[0].name;
        $(this).siblings('.file-name').text(fileName);

        var reader = new FileReader();
        reader.onload = function(e) {
            $('.file-preview').attr('src', e.target.result).removeClass('hidden');
        };
        reader.readAsDataURL(e.target.files[0]);
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');