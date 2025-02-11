from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

# Simple token authentication without proper validation
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Message(BaseModel):
    content: str

# Vulnerable endpoint - No proper authentication or role checking
@app.post("/chat")
async def chat(message: Message, token: str = Depends(oauth2_scheme)):
    """
    Vulnerable endpoint that only checks if a token exists,
    without validating the token or checking user roles
    """
    return {"response": f"Processed message: {message.content}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)