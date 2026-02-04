<div align="center">

<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />

  <h1>Gemini AI Studio - SOTA Edition</h1>

  <p>State-of-the-art Gemini AI chatbot with localhost deployment</p>

  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 🚀 Features

- **🤖 State-of-the-Art AI**: Powered by Google's latest Gemini 2.0 models
- **⚡ Streaming Responses**: Real-time token streaming for faster interactions
- **🎯 Multimodal Support**: Advanced AI capabilities in a clean interface
- **🔒 Localhost Deployment**: Run securely on your own machine
- **⚙️ Configurable**: Adjust temperature, max tokens, and model selection
- **🎨 Modern UI**: Beautiful, responsive interface built with vanilla JavaScript

## 📋 Prerequisites

- Python 3.8 or higher
- A Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

## 🛠️ Installation & Setup

### Quick Start (Recommended)

#### On Linux/macOS:
```bash
./run.sh
```

#### On Windows:
```bash
run.bat
```

The script will:
1. Create a virtual environment
2. Install all dependencies
3. Set up configuration files
4. Start the server

### Manual Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/CarlSp8/Gemini-Antigravity-Jules-CoPilot-Lab.git
   cd Gemini-Antigravity-Jules-CoPilot-Lab
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Gemini API key
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:8000`

## 🔑 Getting Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and paste it in your `.env` file

## 💡 Usage

### Basic Chat
1. Type your message in the input box
2. Press Enter or click the send button
3. Watch as Gemini responds in real-time

### Advanced Features

**Model Selection**: Choose from multiple Gemini models:
- Gemini 2.0 Flash (Experimental) - Latest and fastest
- Gemini 1.5 Pro - Most capable
- Gemini 1.5 Flash - Fast and efficient

**Streaming**: Toggle streaming mode for real-time token generation

**Temperature Control**: Adjust response creativity (0.0 = focused, 2.0 = creative)

**Max Tokens**: Control response length (256-8192 tokens)

## 🏗️ Project Structure

```
Gemini-Antigravity-Jules-CoPilot-Lab/
├── app.py              # FastAPI backend server
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── run.sh             # Linux/macOS startup script
├── run.bat            # Windows startup script
├── static/
│   ├── index.html     # Main HTML page
│   ├── styles.css     # Styling
│   └── app.js         # Frontend JavaScript
└── README.md          # This file
```

## 🔧 API Endpoints

### `GET /`
Serves the main web interface

### `GET /health`
Health check endpoint
```json
{
  "status": "healthy",
  "service": "Gemini AI Studio"
}
```

### `POST /api/chat`
Send a message to Gemini
```json
{
  "message": "Hello, Gemini!",
  "model": "gemini-2.0-flash-exp",
  "temperature": 0.7,
  "max_tokens": 2048,
  "stream": false
}
```

### `GET /api/models`
List available Gemini models

## 🚀 Deployment

### Local Development
The default configuration runs on `127.0.0.1:8000` (localhost only)

### Production Deployment
For production deployment:
1. Update the `HOST` in `.env` to `0.0.0.0`
2. Configure proper security (HTTPS, authentication)
3. Use a production ASGI server (Gunicorn with Uvicorn workers)

## 🔒 Security Notes

- **Never commit your `.env` file** (it's in `.gitignore`)
- Keep your API key secure
- For production, implement proper authentication
- Use HTTPS in production environments

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built with [Google Gemini](https://ai.google.dev/)
- Powered by [FastAPI](https://fastapi.tiangolo.com/)
- Designed with [AI Studio](https://aistudio.google.com/apps)

## 📞 Support

For issues and questions:
- Open an [issue](https://github.com/CarlSp8/Gemini-Antigravity-Jules-CoPilot-Lab/issues)
- Check the [Gemini API docs](https://ai.google.dev/docs)

---

<div align="center">
  Made with ❤️ using Google AI Studio
</div>
