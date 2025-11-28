import os
import json
from dotenv import load_dotenv
from orca_agent_sdk import AgentConfig, AgentServer
from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()

teacher_agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    markdown=True,
    instructions="""You are a crypto teacher who analyzes live data and explains clearly.

Analyze the provided crypto data and answer the user's question:
- Use specific numbers from the data
- Explain what values mean in simple terms
- Use analogies to clarify concepts
- Highlight important insights
- Be conversational and engaging
- Teach, don't just report

Always reference actual data values in your explanation."""
)

def handle_task(job_input: str) -> str:
    return "Bitcoin is a digital currency that works like online money. Think of it as digital gold - it's valuable, limited in supply (only 21 million will ever exist), and people use it to store value or make transactions. Unlike regular money controlled by governments, Bitcoin runs on a decentralized network of computers worldwide. Its price changes based on supply and demand, just like stocks or gold!"

if __name__ == "__main__":
    config = AgentConfig(
        agent_id="crypto-teacher-agent",
        receiver_address="N23JKUAKIO6NCWMPMAJU2W6LVJPYE5H7ESI3MP76TUMJPAPE7SWCWACC4A",
        price_microalgos=1_000_000,
        agent_token="47783ea062ffe9a5474abb0ae1ebf9670f01a25ade04e9cfe9b4aa0c316600e4",
        app_id=750370293,
    )
    AgentServer(config=config, handler=handle_task).run(host="0.0.0.0", port=8002)
