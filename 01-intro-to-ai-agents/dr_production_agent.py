"""
AI Agents for Beginners — Lesson 01
DR Film Production Agent

Demonstrates the core AI Agent loop:
  Perceive → Reason → Act

A foreign production company asks about filming in the Dominican Republic.
The agent uses real tools to answer: productions, incentives, and local services.

Based on: github.com/microsoft/ai-agents-for-beginners
Context:  Dominican Republic film industry

Requirements:
    pip install agent-framework azure-ai-projects azure-identity python-dotenv

Environment variables (.env):
    AZURE_AI_PROJECT_ENDPOINT=your_endpoint_here
    AZURE_AI_MODEL_DEPLOYMENT_NAME=your_model_name_here

Run:
    az login
    python dr_production_agent.py
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


# ── Tools ─────────────────────────────────────────────────────────────────────

@tool(approval_mode="never_require")
def get_productions(production_type: str = "all") -> list[dict]:
    """
    Get a list of international productions filmed in the Dominican Republic.
    Filter by type: 'movie', 'series', or 'all'.
    """
    productions = [
        {
            "title": "Old",
            "year": 2021,
            "type": "movie",
            "studio": "Universal Pictures",
            "location": "Playa El Valle, Samaná",
            "director": "M. Night Shyamalan",
            "stars": ["Gael García Bernal", "Vicky Krieps"],
            "service_company": "Lantica Studios",
        },
        {
            "title": "The Lost City",
            "year": 2022,
            "type": "movie",
            "studio": "Paramount Pictures",
            "location": "Playa Cosón, Samaná",
            "director": "Aaron Nee & Adam Nee",
            "stars": ["Sandra Bullock", "Channing Tatum", "Brad Pitt"],
            "service_company": "Lantica Studios",
        },
        {
            "title": "Shotgun Wedding",
            "year": 2022,
            "type": "movie",
            "studio": "Mandeville Films",
            "location": "Playa Caletón, María Trinidad Sánchez",
            "director": "Jason Moore",
            "stars": ["Jennifer Lopez", "Josh Duhamel"],
            "service_company": "Lantica Studios",
        },
        {
            "title": "Arthur the King",
            "year": 2024,
            "type": "movie",
            "studio": "Lionsgate / eOne Films",
            "location": "Zona Colonial, Santo Domingo",
            "director": "Simon Cellan Jones",
            "stars": ["Mark Wahlberg", "Simu Liu"],
            "service_company": "Lantica Studios",
        },
        {
            "title": "Nyad",
            "year": 2023,
            "type": "movie",
            "studio": "Netflix",
            "location": "Centro Acuático, Santo Domingo",
            "director": "Jimmy Chin & Elizabeth Chai Vasarhelyi",
            "stars": ["Annette Bening", "Jodie Foster"],
            "service_company": "Lantica Studios",
        },
        {
            "title": "Hotel Cocaine",
            "year": 2024,
            "type": "series",
            "studio": "MGM+ Studios",
            "location": "Juan Dolio, San Pedro de Macorís",
            "director": "Guillermo Navarro",
            "stars": ["Danny Pino", "Michael Chiklis"],
            "service_company": "Lantica Studios",
        },
        {
            "title": "Saint X",
            "year": 2023,
            "type": "series",
            "studio": "ABC Signature",
            "location": "Santo Domingo",
            "director": "Tanya Hamilton",
            "stars": ["Alycia Debnam-Carey"],
            "service_company": "Lantica Studios",
        },
        {
            "title": "Sin Límites",
            "year": 2022,
            "type": "series",
            "studio": "Amazon Prime Video",
            "location": "Samaná",
            "director": "Simon West",
            "stars": ["José Coronado", "Álvaro Mel"],
            "service_company": "Lantica Studios",
        },
    ]

    if production_type == "all":
        return productions
    return [p for p in productions if p["type"] == production_type]


@tool(approval_mode="never_require")
def get_incentives() -> dict:
    """
    Get information about the Dominican Republic film tax incentives
    under Law 108-10, Article 39 (modified by Law 82-13).
    """
    return {
        "law": "Law 108-10, Article 39 — Modified by Law 82-13 (June 18, 2013)",
        "administered_by": "DGCINE (Dirección General de Cine)",
        "tax_credit": "25% transferable tax credit on all qualified production expenses",
        "minimum_spend": "USD 500,000",
        "qualifying_expenses": [
            "Pre-production, production, and post-production expenses",
            "Equipment rentals",
            "Local and foreign crew (subject to Dominican crew participation)",
            "Location fees",
            "Services and goods purchased in the DR",
        ],
        "dominican_crew_requirement": "25% minimum (from year 6 of the law onward)",
        "validation_timeline": {
            "dgcine_review": "30 calendar days",
            "full_process_max": "90 calendar days",
        },
        "credit_transferability": "Fully transferable to any natural or legal person",
        "additional_benefits": [
            "18% VAT exemption on production-related expenses",
            "Temporary import of goods and equipment",
        ],
        "notes": (
            "Credits can be used to offset income tax (ISR) "
            "or transferred. Cannot be combined with other incentives "
            "for the same production."
        ),
    }


@tool(approval_mode="never_require")
def get_local_services(category: str = "all") -> list[dict]:
    """
    Get local film production service companies in the Dominican Republic.
    Filter by category: 'studio', 'post_production', 'equipment', or 'all'.
    """
    services = [
        {
            "category": "studio",
            "name": "Lantica Studios",
            "website": "lanticastudios.com",
            "location": "Juan Dolio, San Pedro de Macorís",
            "description": (
                "Full-service production studio. One-stop shop for filming in the DR. "
                "Offers sound stages, water tank, underwater filming facilities, "
                "crew sourcing, location scouting, budgeting, and scheduling. "
                "Has serviced over 60 international productions."
            ),
            "notable_credits": ["Old", "The Lost City", "Nyad", "Hotel Cocaine", "Road House"],
        },
        {
            "category": "studio",
            "name": "La Casita Films",
            "website": "lacasitafilms.com",
            "location": "Santo Domingo",
            "description": (
                "Full film production services: locations, permits, local crew, "
                "equipment, logistics, and line production. "
                "Specializes in connecting international productions with DR infrastructure."
            ),
            "notable_credits": ["Dominican independent and international co-productions"],
        },
        {
            "category": "post_production",
            "name": "Pulpo Post",
            "website": "pulpopost.com",
            "location": "Santo Domingo",
            "description": (
                "Full post-production studio. Services include sound design, "
                "pre-mix, final mix, music composition, dubbing, editing, "
                "color correction, DCP & DCDM, LTO backup, and DIT on set. "
                "Has worked with Netflix, Amazon, Disney, HBO, and Sony Pictures Television."
            ),
        },
        {
            "category": "post_production",
            "name": "La Nave Post Lab",
            "website": "lanavepostlab.com.do",
            "location": "Dominican Republic",
            "description": (
                "Post-production laboratory offering color grading, "
                "finishing, and digital cinema deliverables."
            ),
        },
        {
            "category": "equipment",
            "name": "KC Ettes",
            "website": "kcettes.com",
            "location": "Dominican Republic",
            "description": (
                "Camera and grip equipment rental house. "
                "Serves local and international productions."
            ),
        },
        {
            "category": "equipment",
            "name": "PJ Gaffers",
            "website": "pjgaffers.com",
            "location": "Dominican Republic",
            "description": (
                "Lighting and electrical equipment rental. "
                "Specialized gaffer services for film and TV productions."
            ),
        },
    ]

    if category == "all":
        return services
    return [s for s in services if s["category"] == category]


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

    agent = provider.as_agent(
        name="DRProductionAgent",
        instructions=(
            "You are a knowledgeable film production consultant specializing in "
            "the Dominican Republic as a filming destination. "
            "Your role is to help international production companies understand "
            "what the DR offers: past productions, tax incentives under Law 108-10, "
            "and local service providers. "
            "Always use the available tools to retrieve real data before answering. "
            "Be concise, professional, and specific. "
            "When mentioning incentives, always reference Law 108-10 and DGCINE. "
            "When mentioning studios or services, include their website."
        ),
        tools=[get_productions, get_incentives, get_local_services],
    )

    return agent


# ── Demo ──────────────────────────────────────────────────────────────────────

async def main():
    print("\n" + "=" * 65)
    print("  DR Film Production Agent")
    print("  AI Agents for Beginners — Lesson 01")
    print("  github.com/microsoft/ai-agents-for-beginners")
    print("=" * 65)

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
        print(f"\n[Query {i}]\n{query}")
        print("-" * 65)
        print("Agent: ", end="", flush=True)

        async for chunk in agent.run(query, stream=True):
            print(chunk, end="", flush=True)

        print("\n")

    print("=" * 65)
    print("  Demo complete.")
    print("  Next: Lesson 02 — Exploring Agentic Frameworks")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
