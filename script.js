let input = document.getElementById("userInput");
let button = document.getElementById("submitButton");
let response = document.getElementById("response");
// stores the conversation
let conversationHistory = [];


button.onclick = function() {
    let userText = input.value.trim();
    if (userText === "") {
        return;
    }

    // adds the user's message to the conversation
    conversationHistory.push({
        role: "user",
        content: userText
    });

    // shows the user's message
    response.innerHTML += `
        <div class="user-message">
            <strong>You:</strong> ${userText}
        </div>
    `;

    // shows thinking message
    response.innerHTML += `
        <div class="ai-message" id="thinking">
            <strong>Triton2Go GPT:</strong> Thinking...
        </div>
    `;

    input.value = "";
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: userText,
            history: conversationHistory
        })
    })

    .then(res => res.json())
    .then(data => {
        let thinking = document.getElementById("thinking");
        if (thinking) {
            thinking.remove();
        }

        // adds AI response to conversation history
        conversationHistory.push({
            role: "assistant",
            content: data.reply
        });

        // formats the AI response
        let formattedText = data.reply.replace(/\n/g, "\n\n");

        // shows AI response
        response.innerHTML += `
            <div class="ai-message">
                <strong>Triton2Go GPT:</strong>
                ${marked.parse(formattedText)}
            </div>
        `;
    })

    .catch(error => {
        let thinking = document.getElementById("thinking");
        if (thinking) {
            thinking.remove();
        }
        response.innerHTML += `
            <div class="ai-message">
                <strong>Triton2Go GPT:</strong>
                Sorry, I couldn't reach the server.
            </div>
        `;
        console.error("Error:", error);
    });
};