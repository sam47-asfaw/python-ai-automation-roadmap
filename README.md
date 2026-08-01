# Python AI Automation Roadmap

A 15-week, project-driven study plan for learning **automation scripting in Python** (bots, scraping, data pipelines) **integrated with modern AI tooling** — the Anthropic Claude SDK, Claude Code, tool use, and MCP.

Each week has a clear **focus**, curated **study material**, and a hands-on **deliverable**. Every deliverable builds toward a final capstone that exercises the whole architecture end to end.

---

## Who this is for

Developers who know a little programming and want to build **production-grade automation** that uses LLMs as a first-class component — not just as a chatbot. By the end you'll have a containerized, tested, orchestrated pipeline that scrapes, validates, AI-enriches, and stores data on a schedule.

**Time budget:** ~10–15 hrs/week over 15 weeks. Stretch any week that doesn't click rather than rushing.

---

## Architecture

The roadmap teaches every layer of this reference design:

```
┌─────────────────────────────────────────────────┐
│                  TRIGGER LAYER                    │
│   cron / webhook / event queue / manual CLI       │
└────────────────────┬────────────────────────────┘
                     ▼
┌─────────────────────────────────────────────────┐
│              ORCHESTRATION LAYER                  │
│        Prefect / Dagster (DAG, retries)           │
└────────────────────┬────────────────────────────┘
                     ▼
┌──────────────┬──────────────┬───────────────────┐
│  INGESTION   │  PROCESSING   │   AI/AGENT LAYER   │
│ httpx/       │  pandas/      │  Anthropic SDK     │
│ playwright/  │  polars/      │  + tool use        │
│ DB readers   │  validation   │  + MCP servers     │
└──────┬───────┴──────┬───────┴─────────┬─────────┘
       │              │                 │
       └──────────────┼─────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│                 STORAGE LAYER                     │
│    Postgres / DuckDB / S3 / vector DB             │
└────────────────────┬────────────────────────────┘
                     ▼
┌─────────────────────────────────────────────────┐
│         OBSERVABILITY (cuts across all)           │
│   structlog · cost tracking · alerts · pytest     │
└─────────────────────────────────────────────────┘
```

> **Claude Code vs. the Anthropic SDK:** Claude Code is your *build-time* accelerator (scaffolding, tests, refactors). The Anthropic SDK is your *run-time* AI (the calls your automation makes in production). Keep the two mentally separate.

---

## The Plan

### Phase 1 — Python Foundations (Weeks 1–3)

| Week | Focus | Deliverable |
|------|-------|-------------|
| **1** | Core syntax, control flow, data structures, comprehensions, slicing | Rewrite 5 basic scripts (calculator, file renamer, word counter) from memory |
| **2** | Functions, `*args`/`**kwargs`, decorators, context managers, classes, generators | Class-based inventory tool with a custom context manager |
| **3** | Type hints, `pydantic` v2, `asyncio`/`await`, `httpx` async, `uv` env management | Async script fetching 10 URLs concurrently, validated with Pydantic |

**Study material**
- *Automate the Boring Stuff with Python* — Al Sweigart (free online), chs. 1–6
- *Fluent Python* — Luciano Ramalho (2nd ed), chs. 1, 7, 9, 17
- Official Python Tutorial (docs.python.org), sections 3–5
- Pydantic v2 docs — Models + Validators
- Real Python — "Async IO in Python", decorators & generators tutorials
- `uv` docs (astral.sh)

---

### Phase 2 — Automation Fundamentals (Weeks 4–6)

| Week | Focus | Deliverable |
|------|-------|-------------|
| **4** | `pathlib`, `os`, `shutil`, `subprocess`, `glob`, CSV/JSON/Excel | Folder watcher that sorts files by type and logs actions |
| **5** | `httpx`/`requests`, `BeautifulSoup`, `playwright`, auth/sessions, rate limiting, robots.txt etiquette | Bot that logs into a demo site, extracts a table, exports CSV |
| **6** | `cron`, `APScheduler`, `schedule`, CLIs with `typer`/`click`, config via `.env`/`pydantic-settings` | Package the Week 5 bot as a `typer` CLI that runs on a schedule |

**Study material**
- *Automate the Boring Stuff* — chs. 9–13
- Playwright for Python — official docs
- *Web Scraping with Python* — Ryan Mitchell, chs. 1–4
- Real Python — "Beautiful Soup" guide
- Typer docs (tiangolo), APScheduler docs, crontab.guru

---

### Phase 3 — AI Tooling Layer (Weeks 7–9)

| Week | Focus | Deliverable |
|------|-------|-------------|
| **7** | `anthropic` SDK, Messages API, streaming, content blocks, model selection (Haiku/Sonnet/Opus), token/cost awareness, prompt caching | CLI that summarizes a text file via a streamed Claude response, printing token cost per call |
| **8** | Tool use (function calling), JSON output validated with Pydantic, **Claude Code** for scaffolding/tests/refactors, programmatic tool calling | Claude agent with 2 real tools running a full tool loop |
| **9** | Model Context Protocol (MCP servers), embeddings, vector stores (`chromadb`/`pgvector`), basic RAG | MCP server exposing a Phase 2 script as a Claude-callable tool |

**Study material**
- Claude Platform docs — Quickstart, Messages API, "Tool use" overview (platform.claude.com/docs)
- Anthropic engineering blog — "Advanced tool use"
- `anthropic` Python SDK README (GitHub)
- Claude Code docs (docs.claude.com)
- Model Context Protocol docs (modelcontextprotocol.io) + Anthropic's MCP quickstart
- Chroma or pgvector getting-started guide

> Model lineup as of mid-2026: **Haiku** (fast/cheap, high-volume) → **Sonnet** (best value, most work) → **Opus** (hardest reasoning & agentic coding). Use prompt caching to cut cost on repeated context.

---

### Phase 4 — Data Pipelining (Weeks 10–12)

| Week | Focus | Deliverable |
|------|-------|-------------|
| **10** | ETL patterns, idempotency, incremental vs full loads, `pandas` vs `polars`, `sqlalchemy`, `duckdb` | ETL: API → clean in Polars → load to Postgres/DuckDB, safely re-runnable |
| **11** | DAGs, retries, scheduling, backfills with **Prefect** or **Dagster** (Airflow = legacy alternative) | Convert the Week 10 ETL into an orchestrated flow with retries + schedule |
| **12** | `Celery` + `Redis`/`RabbitMQ`, task queues, decoupling producers/consumers | Queue-based pipeline: scraper enqueues jobs, workers process + AI-enrich |

**Study material**
- *Python for Data Analysis* — Wes McKinney, chs. 5–8
- Polars user guide, DuckDB docs
- Prefect "Getting Started" or Dagster tutorial
- Celery docs "First Steps", Redis Python client docs

---

### Phase 5 — Production (Weeks 13–15)

| Week | Focus | Deliverable |
|------|-------|-------------|
| **13** | Docker, multi-stage builds, `docker-compose` (app + Postgres + Redis), secrets/env management | Containerize the Phase 4 pipeline with compose |
| **14** | `structlog`, `tenacity` retries, rate limiting, LLM cost tracking, `pytest` + mocking API calls | Add structured logging, retries, and a pytest suite (mocked Claude calls) |
| **15** | GitHub Actions (lint/test/build), deployment basics, prod monitoring | **Capstone** (see below) |

**Study material**
- Docker official Python guide + Docker Compose docs
- pytest docs, tenacity docs, structlog docs
- Real Python testing guides
- GitHub Actions docs — "Building and testing Python"

> **Testing tip:** mock the Anthropic client in unit tests so you don't burn tokens. Run a small integration suite (20–50 representative examples) against the real model before shipping any prompt change.

---

## Capstone Project

A single project that touches every layer of the architecture:

> **Scheduled scrape → Pydantic validation → Claude classification/enrichment → Postgres → cost-logged, containerized, CI-tested, orchestrated.**

If you can build and deploy this, you've learned the whole roadmap.

---

## Repo Structure

```
python-ai-automation-roadmap/
├── README.md
├── week-01-core-syntax/
├── week-02-functions-oop/
├── week-03-typing-async/
├── week-04-os-file-automation/
├── week-05-web-scraping-bots/
├── week-06-scheduling-cli/
├── week-07-anthropic-sdk/
├── week-08-tool-use-claude-code/
├── week-09-mcp-retrieval/
├── week-10-etl-dataframes/
├── week-11-orchestration/
├── week-12-queues-async/
├── week-13-containerization/
├── week-14-reliability-observability/
└── week-15-cicd-capstone/
```

Each week folder should contain its own `README.md` (notes + what you built) and the code for that week's deliverable.

---

## Ongoing Habits

- Use **Claude Code** as your pair-programmer from Week 7 onward — but hand-write Phases 1–2 yourself so fundamentals stick.
- Commit daily; one commit per study session minimum.
- Keep a short log in each week's `README.md`: what clicked, what didn't, links you found useful.

---

## License

MIT — do whatever you like with this plan.
#   p y t h o n - a i - a u t o m a t i o n - r o a d m a p  
 