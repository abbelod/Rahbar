async function sendMessage() {
    const input = document.getElementById("user-message");
    const message = input.value.trim();
    if (!message) return;

    // Add user message to chat
    const chatMessages = document.getElementById("chat-messages");
    const userMessageDiv = document.createElement("div");
    userMessageDiv.classList.add("message", "user");
    userMessageDiv.textContent = message;
    chatMessages.appendChild(userMessageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Clear input
    input.value = "";

    // Send the message to the server
    try {
        const response = await fetch("{% url 'chatbot' %}", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": "{{ csrf_token }}",
            },
            body: new URLSearchParams({ message: message }),
        });

        if (response.ok) {
            const data = await response.json();
            const botMessageDiv = document.createElement("div");
            botMessageDiv.classList.add("message", "bot");
            console.log(data.response)
            // botMessageDiv.innerHTML = data.response
            chatMessages.appendChild(botMessageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        } else {
            throw new Error("Failed to get response from server");
        }
    } catch (error) {
        const errorDiv = document.createElement("div");
        errorDiv.classList.add("message", "bot");
        errorDiv.textContent = "Error: Unable to connect to the chatbot.";
        chatMessages.appendChild(errorDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}