// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const modelSelect = document.getElementById('modelSelect');
const streamToggle = document.getElementById('streamToggle');
const temperatureSlider = document.getElementById('temperature');
const temperatureValue = document.getElementById('temperatureValue');
const maxTokensSlider = document.getElementById('maxTokens');
const maxTokensValue = document.getElementById('maxTokensValue');
const statusElement = document.getElementById('status');

// State
let isProcessing = false;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    checkHealth();
});

function setupEventListeners() {
    // Send button
    sendButton.addEventListener('click', sendMessage);
    
    // Enter key to send (Shift+Enter for new line)
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    // Auto-resize textarea
    userInput.addEventListener('input', () => {
        userInput.style.height = 'auto';
        userInput.style.height = userInput.scrollHeight + 'px';
    });
    
    // Temperature slider
    temperatureSlider.addEventListener('input', (e) => {
        temperatureValue.textContent = e.target.value;
    });
    
    // Max tokens slider
    maxTokensSlider.addEventListener('input', (e) => {
        maxTokensValue.textContent = e.target.value;
    });
}

async function checkHealth() {
    try {
        const response = await fetch('/health');
        const data = await response.json();
        updateStatus('Ready', 'healthy');
    } catch (error) {
        updateStatus('Error', 'error');
        console.error('Health check failed:', error);
    }
}

function updateStatus(text, state) {
    const statusText = statusElement.querySelector('span:last-child');
    const statusDot = statusElement.querySelector('.status-dot');
    
    statusText.textContent = text;
    
    if (state === 'healthy') {
        statusDot.style.background = '#34a853';
    } else if (state === 'processing') {
        statusDot.style.background = '#fbbc04';
    } else if (state === 'error') {
        statusDot.style.background = '#ea4335';
    }
}

async function sendMessage() {
    const message = userInput.value.trim();
    
    if (!message || isProcessing) return;
    
    // Clear input
    userInput.value = '';
    userInput.style.height = 'auto';
    
    // Remove welcome message if present
    const welcomeMessage = document.querySelector('.welcome-message');
    if (welcomeMessage) {
        welcomeMessage.remove();
    }
    
    // Add user message
    addMessage(message, 'user');
    
    // Disable input
    isProcessing = true;
    sendButton.disabled = true;
    updateStatus('Processing...', 'processing');
    
    // Prepare request
    const requestData = {
        message: message,
        model: modelSelect.value,
        temperature: parseFloat(temperatureSlider.value),
        max_tokens: parseInt(maxTokensSlider.value),
        stream: streamToggle.checked
    };
    
    try {
        if (streamToggle.checked) {
            await handleStreamingResponse(requestData);
        } else {
            await handleNormalResponse(requestData);
        }
    } catch (error) {
        console.error('Error:', error);
        addErrorMessage('Failed to get response. Please check your API key and try again.');
        updateStatus('Error', 'error');
    } finally {
        isProcessing = false;
        sendButton.disabled = false;
        updateStatus('Ready', 'healthy');
    }
}

async function handleNormalResponse(requestData) {
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData)
    });
    
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Request failed');
    }
    
    const data = await response.json();
    addMessage(data.response, 'assistant');
}

async function handleStreamingResponse(requestData) {
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData)
    });
    
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Request failed');
    }
    
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let accumulatedText = '';
    let messageElement = null;
    
    while (true) {
        const { value, done } = await reader.read();
        
        if (done) break;
        
        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');
        
        for (const line of lines) {
            if (line.startsWith('data: ')) {
                const data = line.slice(6);
                
                if (data === '[DONE]') {
                    continue;
                }
                
                try {
                    const parsed = JSON.parse(data);
                    if (parsed.text) {
                        accumulatedText += parsed.text;
                        
                        if (!messageElement) {
                            messageElement = addMessage(accumulatedText, 'assistant', true);
                        } else {
                            updateMessageContent(messageElement, accumulatedText);
                        }
                    }
                } catch (e) {
                    console.error('Error parsing streaming data:', e);
                }
            }
        }
    }
}

function addMessage(content, role, isStreaming = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}-message`;
    
    const label = document.createElement('div');
    label.className = 'message-label';
    label.textContent = role === 'user' ? 'You' : 'Gemini';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = content;
    
    messageDiv.appendChild(label);
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    return isStreaming ? contentDiv : null;
}

function updateMessageContent(element, content) {
    element.textContent = content;
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function addErrorMessage(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    chatMessages.appendChild(errorDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
