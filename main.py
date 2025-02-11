from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Message(BaseModel):
    content: str

@app.post("/chat")
async def chat(message: Message, token: str = Depends(oauth2_scheme)):
    return {"response": f"Processed message: {message.content}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
