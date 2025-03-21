from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import asyncio

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o")

venv_python = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe") #<--- change here.

server_params = StdioServerParameters(
    command=venv_python,
    args=["math_server.py"]
)

async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools=await load_mcp_tools(session)
            agent = create_react_agent(model, tools)
            math_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is (44+6)x14?"}]})

            print(math_response["messages"][-1].content)

        
if __name__ == "__main__":
    asyncio.run(run_agent())