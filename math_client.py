# math_client.py
import os
import asyncio
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

# Load environment variables
load_dotenv()

async def main():
    # Initialize the language model
    model = ChatOpenAI(model="gpt-4o")

    # Define server parameters
    server_params = StdioServerParameters(
        command="python",
        url: "http://localhost:8000/sse",
        transport: "sse",

        # args=["math_server.py"],  # Ensure this path is correct
    )

    # Connect to the MCP server
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            # Load tools from the MCP server
            tools = await load_mcp_tools(session)

            # Create the agent with the loaded tools
            agent = create_react_agent(model, tools)

            # Example query
            query = "What's (3 + 5) x 12?"

            # Get the agent's response
            agent_response = await agent.ainvoke({"messages": [{"role": "user", "content": query}]})

            # Print the response
            print(agent_response["messages"][-1]["content"])

if __name__ == "__main__":
    asyncio.run(main())
