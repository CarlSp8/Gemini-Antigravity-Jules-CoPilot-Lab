"""
Gemini AI Studio - SOTA Localhost Deployment
A state-of-the-art Gemini AI chatbot with multimodal capabilities.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import Optional
import json

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please copy .env.example to .env and set your API key.")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize FastAPI app
app = FastAPI(
    title="Gemini AI Studio",
    description="State-of-the-art Gemini AI chatbot with localhost deployment",
    version="1.0.0"
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Request models
class ChatRequest(BaseModel):
    message: str
    model: Optional[str] = "gemini-2.0-flash-exp"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 2048
    stream: Optional[bool] = False

class ChatResponse(BaseModel):
    response: str
    model: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main HTML page"""
    try:
        with open("static/index.html", "r") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Welcome to Gemini AI Studio</h1><p>Static files not found. Please ensure the static directory exists.</p>")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Gemini AI Studio"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint with SOTA Gemini features
    Supports streaming and various model configurations
    """
    try:
        # Initialize the model with configuration
        generation_config = {
            "temperature": request.temperature,
            "max_output_tokens": request.max_tokens,
        }
        
        model = genai.GenerativeModel(
            model_name=request.model,
            generation_config=generation_config
        )
        
        # Generate response
        if request.stream:
            # Streaming response
            async def generate_stream():
                response = model.generate_content(request.message, stream=True)
                for chunk in response:
                    if chunk.text:
                        yield f"data: {json.dumps({'text': chunk.text})}\n\n"
                yield "data: [DONE]\n\n"
            
            return StreamingResponse(
                generate_stream(),
                media_type="text/event-stream"
            )
        else:
            # Non-streaming response
            response = model.generate_content(request.message)
            return ChatResponse(
                response=response.text,
                model=request.model
            )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

@app.get("/api/models")
async def list_models():
    """List available Gemini models"""
    try:
        models = []
        for model in genai.list_models():
            if 'generateContent' in model.supported_generation_methods:
                models.append({
                    "name": model.name,
                    "display_name": model.display_name,
                    "description": getattr(model, 'description', 'No description available')
                })
        return {"models": models}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing models: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    
    print(f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║          Gemini AI Studio - SOTA Edition                  ║
    ║                                                           ║
    ║  Server starting on http://{host:<15}:{port:<5}       ║
    ║                                                           ║
    ║  Features:                                                ║
    ║  ✓ Multimodal Gemini AI                                  ║
    ║  ✓ Streaming responses                                   ║
    ║  ✓ State-of-the-art models                              ║
    ║  ✓ Localhost deployment ready                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(app, host=host, port=port)
