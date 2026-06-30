# AI Agents Portfolio

Practical demos built while studying the **[AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** course by Microsoft.

Each demo is grounded in the Dominican Republic film industry — a domain I work in — to make every example original, specific, and professionally relevant.

---

## Structure

| Folder | Lesson | Demo |
|---|---|---|
| `01-intro-to-ai-agents/` | Introduction to AI Agents | DR Film Production Agent |

More lessons coming as the course progresses.

---

## Setup

### Requirements

- Python 3.10+
- Azure account with AI Foundry project
- Azure CLI

### Environment variables

Copy `.env.example` and fill in your credentials:

```bash
cp .env.example .env
```

```env
AZURE_AI_PROJECT_ENDPOINT=https://your-project.api.azureml.ms
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini
```

### Login

```bash
az login
```

---

## Course Reference

- **Course**: [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) — Microsoft
- **My background**: MSc in Artificial Intelligence, UNIR

---

## License

MIT
