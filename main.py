import asyncio

from agent.agent import run_agent

async def main():
    result = await run_agent("why mac is more fast ")
    print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())

