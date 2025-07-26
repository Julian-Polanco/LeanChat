document.addEventListener('DOMContentLoaded', function () {
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const chatBody = document.getElementById('chat-body');


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');


    function appendMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');

        const messageContentDiv = document.createElement('div');
        messageContentDiv.classList.add('message-content');

        if (sender === 'bot') {
            let formattedMessage = message.replace(/\n/g, '<br>');
            formattedMessage = formattedMessage.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            messageContentDiv.innerHTML = formattedMessage;
        } else {
            messageContentDiv.textContent = message;
        }

        messageDiv.appendChild(messageContentDiv);
        chatBody.appendChild(messageDiv);


        chatBody.scrollTop = chatBody.scrollHeight;
    }


    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.id = 'typing-indicator';
        typingDiv.classList.add('message', 'bot-message');

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        contentDiv.innerHTML = '<span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span>';

        typingDiv.appendChild(contentDiv);
        chatBody.appendChild(typingDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    }


    function removeTypingIndicator() {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) {
            indicator.remove();
        }
    }


    chatForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const userMessage = messageInput.value.trim();

        if (userMessage) {

            appendMessage(userMessage, 'user');

            messageInput.value = '';

            showTypingIndicator();


            fetch('/chat/api/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                removeTypingIndicator();
                if (data.response) {
                    appendMessage(data.response, 'bot');
                } else if (data.error) {
                    appendMessage('Error: ' + data.error, 'bot');
                }
            })
            .catch(error => {
                removeTypingIndicator();
                console.error('Error:', error);
                appendMessage('Lo siento, ha ocurrido un error de conexión.', 'bot');
            });
        }
    });
});
