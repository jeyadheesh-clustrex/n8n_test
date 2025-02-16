from fastapi import APIRouter, Depends
from pydantic import BaseModel
from auth import verify_token

chat = APIRouter()

api_secret_key = 'sfafddsf'
class Message(BaseModel):
    content: str

# yes bro

@chat.post("/chat")
async def chat_endpoint(message: Message, token: str):
    """Secure endpoint that validates token before processing."""
    return {"user": token, "response": f"Processed message: {message.content}"}
