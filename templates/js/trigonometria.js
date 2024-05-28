document.getElementById('opcion2').addEventListener('click', function(event) {
    event.preventDefault();
    var modal = document.getElementById('modal');
    modal.style.display = 'flex';
    modal.style.animation = 'fadeIn 0.5s';
});

document.querySelector('.close').addEventListener('click', function() {
    var modal = document.getElementById('modal');
    modal.style.animation = 'fadeOut 0.5s';
    setTimeout(function() {
        modal.style.display = 'none';
    }, 500);
});
