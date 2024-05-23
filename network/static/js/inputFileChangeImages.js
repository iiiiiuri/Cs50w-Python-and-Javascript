function previewProfileImage(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('profile_preview');
        output.src = reader.result;
        output.classList.remove('hidden');
    };
    reader.readAsDataURL(event.target.files[0]);
}

function previewBackgroundImage(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('background_preview');
        output.src = reader.result;
        output.classList.remove('hidden');
    };
    reader.readAsDataURL(event.target.files[0]);
}

function cancelForm() {
    var formDiv = document.getElementById("formDiv");
    var overlay = document.getElementById("overlay");
    var profileInput = document.getElementById("profile_picture");
    var backgroundInput = document.getElementById("background_picture");
    var profilePreview = document.getElementById("profile_preview");
    var backgroundPreview = document.getElementById("background_preview");
    formDiv.style.display = "none";
    overlay.style.display = "none";
    profileInput.value = "";
    backgroundInput.value = "";
    profilePreview.src = "";
    backgroundPreview.src = "";
    profilePreview.classList.add('hidden');
    backgroundPreview.classList.add('hidden');
}

function toggleForm() {
    var formDiv = document.getElementById("formDiv");
    var overlay = document.getElementById("overlay");
    if (formDiv.style.display === "none") {
        formDiv.style.display = "block";
        overlay.style.display = "block";
    } else {
        formDiv.style.display = "none";
        overlay.style.display = "none";
    }
}

function triggerFileSelect(id) {
    document.getElementById(id).click();
}