var body = document.getElementsByTagName('body');
var email_popup = document.getElementById('email-popup-container');
var insta_popup = document.getElementById('insta-popup-container');
var youtube_popup = document.getElementById('youtube-popup-container');
var tiktok_popup = document.getElementById('tiktok-popup-container');
var blog_popup = document.getElementById('blog-popup-container');

function showPopup(obj) {
    if (obj == 'email_popup'){
        console.log('called');
        email_popup.style.display = 'block';}
    else if (obj == 'insta_popup')
        insta_popup.style.display = 'block';
    else if (obj == 'youtube_popup')
        youtube_popup.style.display = 'block';
    else if (obj == 'tiktok_popup')
        tiktok_popup.style.display = 'block';
    else if (obj == 'blog_popup')
        blog_popup.style.display = 'block';
    body[0].style.overflowY = 'hidden';
}

function hidePopup(obj) {
    if (obj == 'email_popup')
        email_popup.style.display = 'none';
    else if (obj == 'insta_popup')
        insta_popup.style.display = 'none';
    else if (obj == 'youtube_popup')
        youtube_popup.style.display = 'none';
    else if (obj == 'tiktok_popup')
        tiktok_popup.style.display = 'none';
    else if (obj == 'blog_popup')
        blog_popup.style.display = 'none';
    body[0].style.overflowY = 'visible';
}

var message = document.getElementById('message');

setTimeout(hideMessage, 4000);
function hideMessage() {
    message.style.display = 'none';
}

