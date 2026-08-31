let input = document.getElementById("userInput");
let button = document.getElementById("submitButton");
let response = document.getElementById("response");

button.onclick = function() {
    response.textContent = input.value;
};