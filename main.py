from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
#from agent import get_agent
from llama_agent import get_llama_agent

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
#llm  = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def read_root():
    print("test")
    return {"message": "Hello, World!"}


# @app.post("/chat")
# async def chat_endpoint(request_data: dict):
#     try:
#         user_input = request_data.get("user_input", "")
#         response = llm.predict(user_input)
#         return {"aiResponse": response}
#     except Exception as e:
#         # Log the exception
#         print(f"Error in chat_endpoint: {e}")
#         # Return a 500 error response
#         return {"error": "Internal Server Error"}, 500

#v1 with langchain
# @app.post("/chat")
# async def chat_endpoint(request_data: dict):
#     try:
#         user_input = request_data.get("user_input", "")
#         agent = get_agent()
#         response = agent.run(user_input, tags = [user_input])
#         return {"aiResponse": response}
#     except Exception as e:
#         # Log the exception
#         print(f"Error in chat_endpoint: {e}")
#         # Return a 500 error response
#         return {"error": "Internal Server Error"}, 500

agent = None
#v2 with llama index abstraction
@app.post("/chat")
async def chat_endpoint(request_data: dict):
    global agent
    try:
        user_input = request_data.get("user_input", "")
        if agent is None:
            # Create the agent if it hasn't been created yet
            agent = get_llama_agent()
        response = agent.chat(user_input)
        return {"aiResponse": str(response)}
    except Exception as e:
        # Log the exception
        print(f"Error in chat_endpoint: {e}")
        # Return a 500 error response
        return {"error": "Internal Server Error"}, 500



# source env/bin/activate
#uvicorn main:app --reload
