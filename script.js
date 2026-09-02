let input = document.getElementById("userInput");
let button = document.getElementById("submitButton");
let response = document.getElementById("response");

button.onclick = function() {
    let userText = input.value;

    response.innerHTML = "<p>Thinking...</p>";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userText })
    })
    .then(res => res.json())
    .then(data => {
        let formattedText = data.reply.replace(/\n/g, "\n\n");
        response.innerHTML = marked.parse(formattedText);
    })
    .catch(error => {
        response.textContent = "Error: Could not reach the server.";
        console.error("Error:", error);
    });
};