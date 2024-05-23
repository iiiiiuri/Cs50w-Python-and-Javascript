var fileInput = document.querySelector('.file-upload .file-input');
var removeButton = document.querySelector('.remove-button');
var filePreview = document.querySelector('.file-upload .file-preview');

document.querySelector('.file-upload .upload-button').addEventListener('click', function() {
    fileInput.click();
});

document.querySelector('.file-upload .file-name').addEventListener('click', function() {
    fileInput.click();
});

fileInput.addEventListener('change', function() {
    var fileName = this.files[0].name;
    document.querySelector('.file-upload .file-name').textContent = fileName;
    removeButton.classList.remove('hidden');

    var reader = new FileReader();
    reader.onload = function (e) {
        filePreview.src = e.target.result;
        filePreview.classList.remove('hidden');
    };
    reader.readAsDataURL(this.files[0]);
});

removeButton.addEventListener('click', function() {
    fileInput.value = '';
    document.querySelector('.file-upload .file-name').textContent = 'No file chosen';
    removeButton.classList.add('hidden');
    filePreview.classList.add('hidden');
});