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

$("#compose_post").on("submit", function(event) {
    event.preventDefault();

    var formData = new FormData();
    formData.append('content', $('#editor').val());
    if ($('.file-input')[0].files[0]) {
        formData.append('image', $('.file-input')[0].files[0]);
    }

    $.ajax({
        url: 'create_post/',  // Substitua por sua URL
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function(response) {
            // Faça algo com a resposta
            location.reload(true)// Força o recarregamento da página
        },
        error: function(response) {
            // Trate o erro
        }
    });
});