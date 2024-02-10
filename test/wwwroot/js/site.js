function openFullScreen(imageSrc) {
    const fullscreenContainer = document.createElement('div');
    fullscreenContainer.classList.add('fullscreen');

    const fullscreenImage = document.createElement('img');
    fullscreenImage.src = imageSrc;

    fullscreenContainer.appendChild(fullscreenImage);
    document.body.appendChild(fullscreenContainer);

    fullscreenContainer.addEventListener('click', closeFullScreen);
}

function closeFullScreen() {
    const fullscreenContainer = document.querySelector('.fullscreen');
    fullscreenContainer.remove();
}

function send() {
    if (document.getElementById("file_input").files.length != 0) { 
    document.getElementById("file_input").hidden = true;
    document.getElementById("text_input").hidden = false;

        $.ajax({
            type: 'POST',
            url: '/',
            contentType: 'application/json',
            dataType: "JSON",
            success: function (r) {
                console.log("RESULT", r);
            },
            error: function (xhr, status, error) {
                var err = eval("(" + xhr.responseText + ")");
                alert(err.Message);
            }
        });
    }
}