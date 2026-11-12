# Evidentia

### Evidence-Grounded AI Research Assistant

Evidentia is an open-source, agentic AI research assistant
designed to investigate complex questions, analyze research
documents, retrieve information from multiple sources,
and generate structured, evidence-grounded reports.

Built with **LangChain, LangGraph, FastAPI, and advanced RAG**,
Evidentia combines document intelligence, autonomous
research capabilities, and persistent AI workflows in
a terminal-first application.

> **Project Status:** Under active development.
> The features described below represent the target
> architecture and planned capabilities.

## Features

### Document Intelligence

- Ingest and process PDF research documents.
- Extract text while preserving source metadata.
- Split documents into context-aware chunks.
- Generate embeddings and index documents.
- Manage indexed documents and ingestion status.
- Process documents asynchronously.

### Advanced Retrieval-Augmented Generation

- Semantic vector search using pgvector.
- Keyword search using PostgreSQL full-text search.
- Hybrid retrieval with Reciprocal Rank Fusion (RRF).
- Query rewriting and expansion.
- Cross-encoder reranking.
- Metadata-aware retrieval.
- Evidence-grounded question answering.
- Verifiable source citations.

### Agentic Research

- Automatically generate multi-step research plans.
- Search local documents and external web sources.
- Dynamically select research tools.
- Execute independent research tasks concurrently.
- Identify information gaps and refine research.
- Compare and reconcile evidence across sources.
- Generate structured research reports.
- Enforce bounded research iterations and cost limits.

### Persistent Research Workflows

- Stateful research orchestration using LangGraph.
- Persistent conversations and research history.
- Context-aware follow-up questions.
- Workflow checkpointing and recovery.
- Human-in-the-loop approval.
- Interruptible and resumable research sessions.

### Research Reports

Generate structured reports containing:

- Executive summaries
- Key findings
- Supporting evidence
- Source citations
- Conflicting findings
- Research limitations
- Suggested follow-up questions

Reports can be exported as Markdown.

### Terminal Interface

Evidentia uses a terminal-first interface powered by
**Typer and Rich**.

The CLI is designed to support:

- Document ingestion and management
- Document search
- Research questions
- Multi-step investigations
- Real-time research progress
- Conversation history
- Research session resumption
- Report viewing and export

No web frontend is required.

## Technology Stack

| Layer                  | Technologies                |
| ---------------------- | --------------------------- |
| Language               | Python 3.12+                |
| API                    | FastAPI, Pydantic v2        |
| AI Framework           | LangChain v1                |
| Workflow Orchestration | LangGraph v1                |
| LLM Provider           | OpenAI                      |
| Embeddings             | OpenAI Embeddings           |
| Database               | PostgreSQL, SQLAlchemy 2    |
| Vector Search          | pgvector                    |
| Keyword Search         | PostgreSQL Full-Text Search |
| Cache & Queue Broker   | Redis                       |
| Background Jobs        | Dramatiq                    |
| Document Processing    | PyMuPDF                     |
| Object Storage         | S3-compatible storage       |
| Web Research           | Tavily                      |
| Terminal Interface     | Typer, Rich                 |
| Observability          | LangSmith, OpenTelemetry    |
| Testing                | pytest, pytest-asyncio      |
| Code Quality           | Ruff, Pyright               |
| Dependency Management  | uv                          |
| Infrastructure         | Docker, Docker Compose      |
| CI                     | GitHub Actions              |

## System Architecture

Evidentia follows a **modular-monolith architecture**,
separating API delivery, application services, document
processing, retrieval, and AI workflow orchestration.

```text
                 ┌───────────────────┐
                 │   Terminal CLI    │
                 │   Typer + Rich    │
                 └─────────┬─────────┘
                           │ HTTP / SSE
                           ▼
                 ┌───────────────────┐
                 │    FastAPI API    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Application Layer │
                 └─────────┬─────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
     ┌─────────────────┐      ┌─────────────────┐
     │ Document & RAG  │      │    LangGraph    │
     │     Engine      │◄─────│ Research Engine │
     └────────┬────────┘      └────────┬────────┘
              │                        │
              ▼                        ▼
     ┌─────────────────┐      ┌─────────────────┐
     │ Hybrid Retrieval│      │ Research Agents │
     │ & Reranking     │      │ & External Tools│
     └────────┬────────┘      └────────┬────────┘
              │                        │
              └────────────┬───────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Evidence Synthesis│
                 │ & Citation Checks │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │  Research Report  │
                 └───────────────────┘
```

### Supporting Infrastructure

**PostgreSQL + pgvector**

- Application and research records
- Document metadata and embeddings
- Semantic and keyword search
- LangGraph checkpoints

**Redis + Dramatiq**

- Background document processing
- Job coordination
- Caching and rate limiting

**S3-Compatible Storage**

- Original research documents
- Generated research artifacts

**LangSmith**

- LLM and tool execution traces
- Workflow observability
- AI evaluations
- Performance analysis

## How Evidentia Works

### 1. Document Ingestion

```text
PDF Upload
    ↓
Text Extraction
    ↓
Metadata-Aware Chunking
    ↓
Embedding Generation
    ↓
PostgreSQL + pgvector
```

Research documents are converted into searchable
representations while retaining their source metadata.

### 2. Hybrid Retrieval

```text
Research Question
        ↓
Query Rewriting
        ↓
┌──────────────────────┐
│                      │
▼                      ▼
Semantic Search    Keyword Search
│                      │
└──────────┬───────────┘
           ↓
   Reciprocal Rank
       Fusion
           ↓
       Reranking
           ↓
    Ranked Evidence
```

Combining semantic and lexical retrieval helps
discover relevant evidence expressed using different
terminology.

Reranking improves the ordering of candidate passages
before they are provided to the language model.

### 3. Agentic Research

```text
Research Question
        ↓
Research Planning
        ↓
Evidence Collection
        ↓
Evidence Evaluation
        ↓
Sufficient Evidence?
     /         \
    No         Yes
    ↓           ↓
Refine       Synthesize
Research     Findings
    │           ↓
    └─→      Verify
             Citations
                ↓
          Research Report
```

LangGraph coordinates the research process using
explicit state, conditional routing, and bounded
execution loops.

LangChain agents provide tool-calling capabilities
where dynamic tool selection is required.

### 4. Evidence-Grounded Reporting

Research findings are linked to retrieved evidence.

Citation validation checks that referenced sources
exist and support the corresponding claims.

When evidence is insufficient, the assistant should
identify uncertainty rather than invent conclusions.

## CLI

The following commands illustrate the planned
terminal interface.

> These commands are design targets and may not be
> available in the current development version.

### Ingest a Document

```bash
evidentia ingest ./papers/research.pdf
```

### List Indexed Documents

```bash
evidentia documents list
```

### Search Documents

```bash
evidentia search "transformer attention mechanism"
```

### Ask a Research Question

```bash
evidentia ask "What are the limitations of RAG?"
```

### Run a Research Investigation

```bash
evidentia investigate \
  "Compare hybrid retrieval and semantic search"
```

### Resume a Research Session

```bash
evidentia resume <run-id>
```

### View Research History

```bash
evidentia history
```

### View a Research Report

```bash
evidentia report <run-id>
```

## Architecture Principles

Evidentia is designed around the following principles:

**Evidence First**

Research conclusions should be grounded in
retrievable and verifiable sources.

**Explicit Orchestration**

Use LangGraph to control research execution,
state transitions, and termination conditions.

**Controlled Autonomy**

Agents operate within defined tool permissions,
iteration limits, and resource budgets.

**Durable Execution**

Research workflows should recover from supported
interruptions without losing committed state.

**Modular Design**

Keep API handling, application logic, retrieval,
agents, and persistence independently testable.

**Measurable Quality**

Evaluate retrieval performance, answer groundedness,
citation correctness, latency, and cost.

**Production Reliability**

Implement observability, security boundaries,
error handling, and reproducible deployment.

## Reliability & Security

The target implementation includes:

- Authentication and authorization
- Resource-level access controls
- Input and document validation
- Prompt-injection defenses
- SSRF protection for web retrieval
- Tool execution restrictions
- Request timeouts and bounded retries
- Idempotent background operations
- Research iteration and cost limits
- Persistent workflow checkpoints
- Structured logging and tracing

Retrieved documents and web pages are treated
as untrusted data, not executable instructions.

## Testing & Evaluation

Evidentia uses automated tests and AI evaluations
to measure both software correctness and research quality.

**Software Testing**

- Unit tests
- Integration tests
- API tests
- Workflow execution tests
- Failure recovery tests

**AI Evaluation**

- Retrieval precision and recall
- Reranking effectiveness
- Answer groundedness
- Citation correctness
- Research completeness
- Tool-use correctness
- Latency and cost

## Project Structure

Planned repository organization:

```text
evidentia/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── documents/
│   │   ├── retrieval/
│   │   ├── research/
│   │   ├── services/
│   │   └── workers/
│   ├── alembic/
│   ├── tests/
│   └── pyproject.toml
├── cli/
│   ├── evidentia_cli/
│   └── pyproject.toml
├── infra/
│   └── compose.yaml
├── evals/
├── docs/
├── .github/
│   └── workflows/
├── SPEC.md
└── README.md
```

## Development Status

**Evidentia is currently under development.**

The architecture and technology stack are defined,
but not all documented capabilities are implemented.

Installation, configuration, and deployment
instructions will be added as the corresponding
components become available.

See [SPEC.md](SPEC.md) for the full technical
specification and acceptance criteria.

## License

License information will be added when a license
is selected.

---

**Evidentia** — Research backed by evidence.
