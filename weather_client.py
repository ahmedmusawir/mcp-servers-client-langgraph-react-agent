import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI


# Load environment variables
load_dotenv()

async def main():
    model = ChatOpenAI(model="gpt-4o")

    async with MultiServerMCPClient(
        {
            "math": {
                "url": "http://localhost:8001/sse",
                "transport": "sse",
            },
            "weather": {
                # make sure you start your weather server on port 8000
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            }
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        
        # # Test math operations
        math_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is 10 plus 5?"}]})
        print("Math Response:", math_response["messages"][-1].content)


        # Test weather query
        weather_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather in New York?"}]})
        print("Weather Response:", weather_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
