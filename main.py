from auth import verify_token
from fastapi import FastAPI, Depends
from profile import get_profile
from chat import chat
from settings import get_settings

app = FastAPI()

app.include_router(chat, tags=["chat"])
app.include_router(get_profile)
app.include_router(get_settings)

# hai bro

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port="8000")
