"""
AI Agents for Beginners — Lesson 01
DR Film Production Agent

Demonstrates the core AI Agent loop:
  Perceive → Reason → Act

Based on: github.com/microsoft/ai-agents-for-beginners
Context:  Dominican Republic film industry

Run:
    az login
    python3 dr_production_agent.py
"""

import asyncio
import os
import logging
import dotenv

logging.getLogger("agent_framework.foundry").setLevel(logging.ERROR)
dotenv.load_dotenv(dotenv.find_dotenv())

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from agent_framework import tool

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.live import Live

from data import PRODUCTIONS, INCENTIVES, SERVICES

console = Console()


# ── Tools ───────────────────────────────────────────────────────────────────

@tool(approval_mode="never_require")
def get_productions(production_type: str = "all") -> list[dict]:
    """Get international productions filmed in the DR. Filter: 'movie', 'series', 'all'."""
    if production_type == "all":
        return PRODUCTIONS
    return [p for p in PRODUCTIONS if p["type"] == production_type]


@tool(approval_mode="never_require")
def get_incentives() -> dict:
    """Get DR film tax incentives under Law 108-10, Article 39."""
    return INCENTIVES


@tool(approval_mode="never_require")
def get_local_services(category: str = "all") -> list[dict]:
    """Get local film services. Filter: 'studio', 'post_production', 'equipment', 'all'."""
    if category == "all":
        return SERVICES
    return [s for s in SERVICES if s["category"] == category]


# ── Agent setup ───────────────────────────────────────────────────────────────

def build_agent():
    endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
    model = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME")

    if not endpoint or not model:
        raise ValueError(
            "\nMissing environment variables.\n"
            "Set AZURE_AI_PROJECT_ENDPOINT and "
            "AZURE_AI_MODEL_DEPLOYMENT_NAME in your .env file.\n"
        )

    provider = FoundryChatClient(
        project_endpoint=endpoint,
        model=model,
        credential=AzureCliCredential(),
    )

    return provider.as_agent(
        name="DRProductionAgent",
        instructions=(
            "You are a knowledgeable film production consultant specializing in "
            "the Dominican Republic as a filming destination. "
            "Always use the available tools to retrieve real data before answering. "
            "Be concise, professional, and specific. "
            "When mentioning incentives, always reference Law 108-10 and DGCINE. "
            "When mentioning studios or services, include their website."
        ),
        tools=[get_productions, get_incentives, get_local_services],
    )


# ── Demo ──────────────────────────────────────────────────────────────────────

async def main():
    console.print(Panel.fit(
        "[bold cyan]DR Film Production Agent[/bold cyan]\n"
        "[dim]AI Agents for Beginners — Lesson 01[/dim]\n"
        "[dim]github.com/microsoft/ai-agents-for-beginners[/dim]",
        border_style="cyan"
    ))

    agent = build_agent()

    queries = [
        (
            "We're a US production company exploring the Caribbean for our next "
            "action feature. What major productions have filmed in the Dominican Republic?"
        ),
        (
            "That's impressive. What financial incentives does the DR offer "
            "for foreign productions, and who administers them?"
        ),
        (
            "We'd need a full-service studio with water facilities and solid "
            "post-production. What do you recommend locally?"
        ),
    ]

    for i, query in enumerate(queries, 1):
        console.print(f"\n[bold yellow]Query {i}[/bold yellow]")
        console.print(f"[italic]{query}[/italic]\n")

        response_text = ""
        with Live(console=console, refresh_per_second=15) as live:
            async for chunk in agent.run(query, stream=True):
                response_text += str(chunk)
                live.update(Markdown(response_text))

        console.print("[dim]" + "─" * 65 + "[/dim]")

    console.print(Panel.fit(
        "[bold green]Demo complete[/bold green]\n"
        "[dim]Next: Lesson 02 — Explore Agentic Frameworks[/dim]",
        border_style="green"
    ))


if __name__ == "__main__":
    asyncio.run(main())