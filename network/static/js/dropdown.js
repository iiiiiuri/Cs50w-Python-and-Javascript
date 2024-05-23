document.addEventListener('DOMContentLoaded', function() {
    var dropdowns = document.getElementsByClassName('dropdownDotsHorizontal');
    var buttons = document.getElementsByClassName('dropdownMenuIconHorizontalButton');

    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function(event) {
            event.stopPropagation();
            dropdowns[i].classList.toggle('hidden');
        });
    }

    window.addEventListener('click', function() {
        for (let dropdown of dropdowns) {
            if (!dropdown.classList.contains('hidden')) {
                dropdown.classList.add('hidden');
            }
        }
    });
});