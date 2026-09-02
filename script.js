let input = document.getElementById("userInput");
let button = document.getElementById("submitButton");
let response = document.getElementById("response");

button.onclick = function() {
    let userText = input.value;
    response.textContent = "Thinking...";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userText })
    })
    .then(res => res.json())
    .then(data => {
        response.textContent = data.reply;
    })
    .catch(error => {
        response.textContent = "Error: Could not reach the server.";
        console.error("Error:", error);
    });
};