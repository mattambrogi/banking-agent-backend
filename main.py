from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from llama_agent import get_llama_agent
import asyncio

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://banking-agent.up.railway.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

@app.get("/")
def read_root():
    print("test")
    return {"message": "Hello, World!"}

max_retries = 3
backoff_factor = 2

agent = None

@app.post("/chat")
async def chat_endpoint(request_data: dict):
    global agent
    retries = 0
    while retries < max_retries:
        try:
            user_input = request_data.get("user_input", "")
            if agent is None:
                # Create the agent if it hasn't been created yet
                agent = get_llama_agent()
            response = agent.chat(user_input)
            return {"aiResponse": str(response)}
        except Exception as e:
            retries += 1
            # Log the exception
            print(f"Error in chat_endpoint: {e}")
            if retries < max_retries:
                await asyncio.sleep(backoff_factor ** retries)
            else:
            # Return a 500 error response
                return {"error": "Internal Server Error"}, 500



# source env/bin/activate
# uvicorn main:app --reload
