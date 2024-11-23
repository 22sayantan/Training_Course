const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.querySelector('.chat-messages');

sendButton.addEventListener('click', () => {
    const userMessage = messageInput.value;
    if (userMessage.trim() !== '') {
        addMessage('user', userMessage);
        // You can add your API call or backend logic here to send the message
        // and receive a response. For now, let's simulate an AI response:
        setTimeout(() => {
            addMessage('ai', "I'm processing your request. Here's a response:");
        }, 1000); // Simulate a 1-second delay
        messageInput.value = '';
    }
});

function addMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// ... (rest of the JavaScript code)

sendButton.addEventListener('click', () => {
    const userMessage = messageInput.value;
    if (userMessage.trim() !== '') {
        addMessage('user', userMessage);

        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            addMessage('ai', data.response);
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('ai', 'An error occurred. Please try again.');
        });

        messageInput.value = '';
    }
});