var password2 = document.getElementById('password2');
var validation_box = document.getElementById('validation-box');
var characters = document.getElementById('characters');
var upper = document.getElementById('upper');
var lower = document.getElementById('lower');
var symbol = document.getElementById('symbol');
var number = document.getElementById('number');
password2.onkeyup = function () {
    validation_box.style.display = 'block';
    var lowerCase = /[a-z]/g;
    if (password2.value.match(lowerCase))
        lower.classList.replace("red", "green");
    else
        lower.classList.replace("green", "red");

    var upperCase = /[A-Z]/g;
    if (password2.value.match(upperCase))
        upper.classList.replace("red", "green");
    else
        upper.classList.replace("green", "red");

    var numberCase = /[0-9]/g;
    if (password2.value.match(numberCase))
        number.classList.replace("red", "green");
    else
        number.classList.replace("green", "red");

    if (password2.value.length >= 8)
        characters.classList.replace("red", "green");
    else
        characters.classList.replace("green", "red");

    var symbolCase = /[!@#$%^&*_=+-]/g;
    if (password2.value.match(symbolCase))
        symbol.classList.replace("red", "green");
    else
        symbol.classList.replace("green", "red");
}
password2.onblur = function () {
    validation_box.style.display = 'none';
}