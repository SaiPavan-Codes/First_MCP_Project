import os

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
load_dotenv()


async def run_agent(user_input_prompt: str):
    client = MultiServerMCPClient(
        {

            "Bright Data": {
                "command": "npx",
                "args": ["@brightdata/mcp"],
                "env": {
                    "API_TOKEN": os.getenv("BRIGHT_DATA_TOKEN"),
                    "BROWSER_ZONE": os.getenv("BROWSER_ZONE", "scraping_browser")
                 },
                "transport": "stdio",
             },
            # We can add the servers in future right now I am just adding the bright data server just for learning.
        }
    )
    tools = await client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-120b",temperature= 1,api_key=os.getenv("GROQ_API_KEY"))
    agent = create_react_agent(model, tools, prompt=" you are the web search agent with bright tool")
    agent_response = await agent.ainvoke({"messages":user_input_prompt})
    return agent_response

