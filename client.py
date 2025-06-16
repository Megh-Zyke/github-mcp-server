from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import os
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["githubserver.py"],  # Ensure abs path
                "transport": "stdio",
            },
        }
    )
    
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    model = ChatGroq(model = "qwen-qwq-32b")

    agent = create_react_agent(
        model, tools
    )

    repo = "Megh-Zyke/Efficiency-Benchmark"
    predecessor = f"You are an AI assistant that answers questions about the repository {repo}.\n"
    prompt = input("Enter your question: ")

    response = await agent.ainvoke(
        {"messages" : [{"role": "user", "content": predecessor + prompt}]},
    )

    print(response["messages"][-1].content)


asyncio.run(main())