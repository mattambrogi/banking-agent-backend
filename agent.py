# from langchain.agents import AgentType, initialize_agent
# from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
# from langchain.chat_models import ChatOpenAI
# from langchain.tools import BaseTool, StructuredTool, Tool, tool
# from langchain.agents.agent_types import AgentType
# from langchain.callbacks.manager import (
#     AsyncCallbackManagerForToolRun,
#     CallbackManagerForToolRun,
# )
# import pandas as pd
# from typing import Optional, Type
# from dotenv import load_dotenv

# load_dotenv()
# from langchain.llms import OpenAI
# llm = ChatOpenAI(model_name="gpt-4", temperature=0)



# class AnalyzeTransactionsTool(BaseTool):
#   """
#   Analyzes the provided transactions in regards to a user query.
#   Transactions have a date, description, category, amount, and balance.
#   Negative amount indicates money spent. Positive amount indicates money deposited.
#   """

#   name = "analyze_transactions"
#   description = "Used to analyze bank feed transactions"

#   def __init__(self):
#         super().__init__()

#   def _run(self, query_params = None, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
#     """
#     Use the tool
#     Transactions have a date, description, category, amount, and balance.
#     Negative amount indicates money spent. Positive amount indicates money deposited.
#     Make sure you filter by date if asked to do so
#     """
#     df = pd.read_json('mock-transactions.json')
#     pandas_agent = create_pandas_dataframe_agent(
#         llm,
#         df,
#         verbose=True,
#         handle_parsing_erros=True,
#         agent_type=AgentType.OPENAI_FUNCTIONS
#     )
#     answer = pandas_agent.run(run_manager.tags[0])
#     return answer

#   async def _arun(
#         self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
#     ) -> str:
#         """Use the tool asynchronously."""
#         raise NotImplementedError("custom_search does not support async")

# tools = [AnalyzeTransactionsTool()]

# def get_agent():
#     agent = initialize_agent(
#         llm=llm,
#         tools=tools,
#         handle_parsing_errors=True,
#         verbose=True,
#         agent_type=AgentType.OPENAI_FUNCTIONS,
#     )
#     return agent