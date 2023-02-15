window.addEventListener('load', function () {
    var loader = document.getElementById('preloader');
    loader.style.display = 'none';
})

if (document.getElementById('slider-row')) {
    $('#slider-row').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        dots: true,
        autoplaySpeed: 5000,
        prevArrow: '<i id="prev" class="fas fa-chevron-left"></i>',
        nextArrow: '<i id="next" class="fas fa-chevron-right"></i>'
    });
}

function showMenu(page) {
    var navLinks = document.getElementById('navLinks');
    if (page == 'index')
        navLinks.style.right = "0";
    else if (page == 'campaigns')
        navLinks.style.left = "0";
}
function hideMenu(page) {
    var navLinks = document.getElementById('navLinks');
    if (page == 'index')
        navLinks.style.right = "-100%";
    else if (page == 'campaigns')
        navLinks.style.left = "-100%";
}

function get_registration_var() {
    var password1 = document.getElementById('password1');
    var toggle_password1 = document.getElementById('toggle-password1');
    var password2 = document.getElementById('password2');
    var toggle_password2 = document.getElementById('toggle-password2');
    var sign_up = document.getElementById('signup');
    var log_in = document.getElementById('login');
    var side_content = document.getElementById('side-content');
    var top_button_toggler = document.getElementById('top-button-toggler');
    var registration_var = new Array(password1,
        toggle_password1,
        password2,
        toggle_password2,
        sign_up,
        log_in,
        side_content,
        top_button_toggler)
    return registration_var
}
function showPassword1() {
    element = get_registration_var()
    if (element[0].type === 'password') {
        element[0].type = 'text';
        element[1].classList.replace("fa-eye-slash", "fa-eye");
    }
    else {
        element[0].type = 'password';
        element[1].classList.replace("fa-eye", "fa-eye-slash");
    }
}
function showPassword2() {
    element = get_registration_var()
    if (element[2].type === 'password') {
        element[2].type = 'text';
        element[3].classList.replace("fa-eye-slash", "fa-eye");
    }
    else {
        element[2].type = 'password';
        element[3].classList.replace("fa-eye", "fa-eye-slash");
    }
}
function signup() {
    element = get_registration_var()
    element[4].classList.add('active');
    element[5].classList.remove('active');
    element[6].classList.replace('right', 'left');
}
function login() {
    element = get_registration_var()
    element[4].classList.remove('active');
    element[5].classList.add('active');
    element[6].classList.replace('left', 'right');
}
function loginTop() {
    element = get_registration_var()
    element[7].style.left = "0";
    element[5].style.opacity = '1';
    element[5].style.visibility = 'visible';
    element[4].style.opacity = '0';
    element[4].style.visibility = 'hidden';
    element[7].classList.replace('left', 'right');
}
function signupTop() {
    element = get_registration_var()
    element[7].style.left = "50%";
    element[5].style.opacity = '0';
    element[5].style.visibility = 'hidden';
    element[4].style.opacity = '1';
    element[4].style.visibility = 'visible';
    element[7].classList.replace('right', 'left');
}

var message = document.getElementById('message');
if (message) {
    setTimeout(hideMessage, 4000);
    function hideMessage() {
        message.style.display = 'none';
    }
}

if (document.getElementById('campaign-carousel')) {
    var carousel_image = document.getElementById('campaign-carousel');
    var images = new Array(
        "/static/Images/campaigns-carousel1.jpg",
        "/static/Images/campaigns-carousel2.jpg",
        "/static/Images/campaigns-carousel3.jpg",
    );
    var len = images.length;
    var c = 0;
    carousel_slider();
    function carousel_slider() {
        if (c > len - 1) {
            c = 0;
        }
        carousel_image.style.backgroundImage = `url('${images[c]}')`;
        c++;
        setTimeout('carousel_slider()', 4000);
    }
}

var user_icon = document.getElementById('user-icon');
var menu = document.getElementById('menu');
var x = -100;
if (user_icon && menu) {
    user_icon.addEventListener('click', function () {
        if (x == -100) {
            x = 0
            menu.style.right = x;
            menu.style.opacity = 1;
        }
        else {
            x = -100
            menu.style.right = x + '%';
            menu.style.opacity = 0;
        }
    })
}

function showPopup(obj) {
    var body = document.getElementsByTagName('body');
    var email_popup = document.getElementById('email-popup-container');
    var insta_popup = document.getElementById('insta-popup-container');
    var youtube_popup = document.getElementById('youtube-popup-container');
    var tiktok_popup = document.getElementById('tiktok-popup-container');
    var blog_popup = document.getElementById('blog-popup-container');
    if (obj == 'email_popup') {
        console.log('called');
        email_popup.style.display = 'block';
    }
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
    var body = document.getElementsByTagName('body');
    var email_popup = document.getElementById('email-popup-container');
    var insta_popup = document.getElementById('insta-popup-container');
    var youtube_popup = document.getElementById('youtube-popup-container');
    var tiktok_popup = document.getElementById('tiktok-popup-container');
    var blog_popup = document.getElementById('blog-popup-container');
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
