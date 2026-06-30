# Lesson 01 — Introduction to AI Agents

## DR Film Production Agent

A practical demo based on **Lesson 01 of the [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) course by Microsoft**.

This agent demonstrates the core AI Agent loop:

```
Perceive → Reason → Act
```

A foreign production company queries the agent about filming in the Dominican Republic. The agent uses three tools to answer with real, structured data.

---

## What This Agent Does

| Tool | What it returns |
|---|---|
| `get_productions()` | International films and series shot in the DR |
| `get_incentives()` | Law 108-10 tax credit details (DGCINE) |
| `get_local_services()` | Studios, post-production houses, equipment rental |

---

## Setup

### 1. Install dependencies

```bash
pip install -r ../../requirements.txt
```

### 2. Configure environment variables

```bash
cp ../../.env.example .env
```

Fill in your Azure AI Foundry endpoint and model name.

### 3. Login with Azure CLI

```bash
az login
```

### 4. Run the demo

```bash
python dr_production_agent.py
```

---

## Key Concepts (Lesson 01)

- **Tools**: Python functions decorated with `@tool` that the agent can call
- **Instructions**: A system prompt that defines the agent's persona and behavior
- **Streaming**: Responses arrive token by token in real time
- **Perceive → Reason → Act**: The agent reads the query, selects the right tool, and produces a grounded response

---

## Data Sources

- Productions: [Lantica Studios Credits](https://lanticastudios.com/credits)
- Incentives: Law 108-10, Article 39 — DGCINE
- Services: [Lantica Studios](https://lanticastudios.com) · [La Casita Films](https://lacasitafilms.com) · [Pulpo Post](https://pulpopost.com) · [La Nave Post Lab](https://lanavepostlab.com.do) · [KC Ettes](https://kcettes.com) · [PJ Gaffers](https://pjgaffers.com)

---

## Course Reference

- **Course**: [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) by Microsoft
- **Lesson**: 01 — Introduction to AI Agents and Agent Use Cases
- **Original notebook**: `code_samples/01-python-agent-framework.ipynb`
