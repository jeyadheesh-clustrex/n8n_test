from fastapi import FastAPI, Depends
from auth import verify_token
from chat import chat
from profile import get_profile
from settings import get_settings

app = FastAPI()

username = "john_doe"
threshold = 2

app.include_router(chat)
app.include_router(get_profile)
app.include_router(get_settings)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
