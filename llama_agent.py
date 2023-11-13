from llama_index.agent import OpenAIAssistantAgent
from dotenv import load_dotenv
load_dotenv()
import pandas as pd

def get_llama_agent ():
    df = pd.read_json('mock-transactions.json')
    df.to_csv('transactions.csv', index=False)
    agent = OpenAIAssistantAgent.from_new(
        name="Banking Analysis Assistant",
        instructions="You are a personal assistant which analyzes a users banking data. You take the user query and analyze the provided bank transactions file to get an answer. Keep responses brief and concise. Answers should be no more than 75 words.",
        openai_tools=[{"type": "code_interpreter"}],
        files=['transactions.csv'],
    )
    return agent
