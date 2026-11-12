# Evidentia — Project Specification

**Version:** 1.0  
**Status:** Approved Architecture / Pre-Implementation  
**Project Type:** Production-Oriented Agentic AI Research Assistant  
**Primary Interface:** Terminal CLI  
**Development Approach:** Project-Based AI Engineering

---

## 1. Project Identity

**Name:** Evidentia

**Description:**

Evidentia is an agentic AI research platform that combines
retrieval-augmented generation (RAG), document intelligence,
web research, and stateful AI workflows to produce
evidence-grounded research answers and reports.

The system can ingest research documents, retrieve relevant
information, investigate research questions, evaluate
evidence, and generate structured reports with citations.

### GitHub Repository

- Repository: EslamKamel89/evidentia
- URL: https://github.com/EslamKamel89/evidentia
- Clone URL: https://github.com/EslamKamel89/evidentia.git
- Default Branch: main

### Single Source of Truth (SSOT)

The GitHub repository is the authoritative source for:

- Application source code
- Dependencies and lockfiles
- Database migrations
- Architecture decisions
- Technical documentation
- Tests and evaluations
- Infrastructure configuration
- Implementation progress

ChatGPT conversations, course transcripts, and external
examples are learning resources, not authoritative records
of the current implementation.

Before implementing a feature:

1. Inspect the relevant repository files.
2. Understand the existing implementation.
3. Follow established architectural conventions.
4. Verify dependency versions and supported APIs.
5. Avoid duplicating existing functionality.
6. Implement changes compatible with the current codebase.
7. Update affected tests and documentation.

Never assume code exists merely because it was discussed
in a previous conversation.

If the specification and implementation disagree, identify
the discrepancy explicitly. Do not silently treat existing
code as an approved change to the specification.

---

## 2. Project Goals

### Primary Goal

Build a production-oriented AI research assistant using
modern LangChain and LangGraph architecture.

### Engineering Goals

1. Understand advanced RAG architecture and retrieval.
2. Build robust document ingestion pipelines.
3. Implement hybrid search and reranking.
4. Understand LangGraph state and workflow execution.
5. Implement bounded, tool-using AI agents.
6. Build multi-step research workflows.
7. Support persistent conversations and research jobs.
8. Produce evidence-grounded answers with citations.
9. Build asynchronous and recoverable AI workflows.
10. Implement observability, testing, and evaluation.
11. Design scalable, maintainable AI backend systems.
12. Deploy the application using production principles.

### Learning Philosophy

The project prioritizes understanding over copying code.

For every important implementation decision, explain:

- What problem it solves.
- Why the problem matters.
- How the mechanism works.
- How data and control flow through the implementation.
- What alternatives exist.
- What trade-offs were considered.
- What could fail in production.

Use existing backend engineering knowledge as a foundation.

Do not introduce complexity solely to demonstrate
additional frameworks or architectural patterns.

---

## 3. Project Scope

### In Scope

- Terminal-based research interface
- FastAPI backend
- PDF ingestion
- Document extraction and chunking
- Embeddings and vector indexing
- Semantic retrieval
- Keyword and hybrid retrieval
- Query rewriting
- Reranking
- Conversation management
- LangGraph research orchestration
- Tool-calling research agents
- Web research
- Research planning
- Iterative evidence gathering
- Evidence verification
- Structured research reports
- Persistent research workflows
- Human-in-the-loop operations
- Background processing
- Streaming progress
- Observability
- Automated testing and evaluation
- Security and cost controls
- Docker-based deployment

### Out of Scope for Initial Development

- Next.js or a JavaScript frontend
- Mobile applications
- Microservices
- Kubernetes
- Complex multi-agent hierarchies
- Distributed vector databases
- Large-scale document crawling
- Model fine-tuning
- Custom embedding model training

Streamlit may be introduced later if a visual research
dashboard becomes necessary.

It is not part of the initial implementation.

---

## 4. Approved Technology Stack

### Language and Tooling

- Python 3.12+ (choose a tested supported runtime)
- uv for dependency management
- Ruff for linting and formatting
- Pyright for static type checking
- pytest for testing
- pytest-asyncio for asynchronous tests

### Backend

- FastAPI
- Pydantic v2
- Pydantic Settings
- SQLAlchemy 2.x
- Alembic
- HTTPX

### AI Engineering

- LangChain v1 architecture
- LangGraph v1 architecture
- langchain-core
- langchain-openai
- OpenAI API
- LangSmith

Use currently supported LangChain and LangGraph APIs.

Preferred APIs include:

- langchain.agents.create_agent
- langgraph.graph.StateGraph
- langgraph.graph.START
- langgraph.graph.END
- LangGraph checkpointing
- Pydantic-based structured outputs

Use LangChain for models, prompts, tools, and agents.

Use LangGraph for research workflow orchestration,
state transitions, persistence, and controlled execution.

Avoid deprecated APIs and obsolete agent patterns.

### Database

- PostgreSQL
- pgvector
- SQLAlchemy ORM
- Alembic migrations

PostgreSQL stores application records and research metadata.

pgvector supports semantic similarity retrieval.

PostgreSQL full-text search supports keyword retrieval.

### Cache and Background Processing

- Redis
- Dramatiq

Redis supports caching, rate limiting, and background
job coordination.

Dramatiq handles asynchronous ingestion and processing jobs.

LangGraph manages the internal execution of research
workflows.

Background jobs must not replace LangGraph's checkpointing
or workflow state management.

### Document Processing

- PyMuPDF
- LangChain document abstractions
- RecursiveCharacterTextSplitter
- Metadata-aware chunking

### AI Models

Initial provider: OpenAI

Initial embedding model:
text-embedding-3-small

Chat and reasoning models must be configurable rather
than hardcoded throughout the application.

Model selection should consider:

- Task complexity
- Accuracy
- Context requirements
- Latency
- Token usage
- Operational cost

### Retrieval

- PostgreSQL full-text search
- pgvector semantic similarity
- Hybrid retrieval
- Reciprocal Rank Fusion (RRF)
- Cross-encoder reranking
- Query rewriting and expansion

### External Research

- Tavily API for web search
- HTTPX for permitted HTTP retrieval
- Source extraction and normalization

### Storage

- S3-compatible object storage
- Local development storage supported

### Terminal Interface

- Typer
- Rich
- Optional Prompt Toolkit

### Infrastructure

- Docker
- Docker Compose
- Environment-based configuration
- GitHub Actions for CI

---

## 5. High-Level Architecture

```text
Terminal CLI (Typer + Rich)
           |
           v
       FastAPI
           |
           v
  Application Services
           |
           v
  LangGraph Orchestrator
           |
    +------+------+
    |             |
    v             v
Document       Web Research
Research       Tools
    |             |
    +------+------+
           |
           v
    Evidence Pipeline
           |
           v
   Answer Synthesis
           |
           v
   Citation Validation
           |
           v
    Research Report
```

### Supporting Infrastructure

```text
PostgreSQL + pgvector
    - Application records
    - Research metadata
    - Document chunks
    - Vector embeddings
    - Workflow checkpoints

Redis
    - Cache
    - Queue broker
    - Rate limiting

Object Storage
    - Original documents
    - Generated reports
    - Research artifacts

LangSmith
    - LLM traces
    - Agent execution traces
    - Evaluations
    - Debugging
```

---

## 6. Architectural Principles

### 6.1 Modular Monolith

The backend follows a modular-monolith architecture.

Application modules remain logically separated without
requiring independent services.

Primary modules:

- API
- Core configuration
- Database
- Documents
- Retrieval
- Research
- Services
- Workers
- Observability

Avoid premature microservices.

### 6.2 Separation of Responsibilities

FastAPI handles HTTP concerns.

Application services coordinate business operations.

Repositories handle persistence.

Retrieval components handle evidence discovery.

LangChain components handle model interactions and tools.

LangGraph handles workflow orchestration and state.

Workers handle background execution.

The CLI handles user interaction.

Business logic must not be embedded directly in API routes,
CLI commands, or database models.

### 6.3 Explicit Dependencies

Use dependency injection for:

- Database sessions
- LLM clients
- Embedding models
- Vector stores
- External APIs
- Storage services
- Research services

Avoid hidden global dependencies.

### 6.4 Async Where Appropriate

Use asynchronous execution for I/O-bound operations.

Examples:

- HTTP requests
- Database operations
- LLM requests
- Streaming
- External search

Use workers for operations that should outlive HTTP requests.

Do not block the event loop with synchronous CPU-intensive
document processing.

### 6.5 Incremental Implementation

Begin with the smallest working vertical slice.

Introduce advanced functionality only after its underlying
components are implemented and tested.

Every phase should deliver observable working behavior.

---

## 7. Core Functional Requirements

### FR-01: Document Ingestion

Users must be able to ingest local PDF documents.

The ingestion pipeline must:

1. Accept a document.
2. Validate file type and size.
3. Store the original document.
4. Create a document record.
5. Extract text.
6. Preserve page-level source metadata.
7. Split text into chunks.
8. Generate embeddings.
9. Index chunks.
10. Track ingestion status.

Ingestion must support failure reporting and retries.

Repeated ingestion must not silently create duplicate
document records and chunks.

### FR-02: Document Management

Users must be able to:

- List indexed documents.
- Inspect document metadata.
- View ingestion status.
- Delete documents.
- Reindex documents.

Document deletion must handle database records, vectors,
and stored files consistently.

### FR-03: Semantic Search

Users must be able to search indexed documents using
semantic similarity.

Retrieval results should include:

- Chunk identifier
- Document identifier
- Relevant text
- Page number, when available
- Source metadata
- Similarity score, where supported

### FR-04: Hybrid Retrieval

The retrieval engine must support:

- Semantic search
- Keyword search
- Metadata filtering
- Result fusion
- Reranking

Retrieval strategies must be independently testable.

The system must allow comparison against simpler retrieval
baselines.

### FR-05: Research Questions

Users must be able to ask questions against indexed
documents.

The assistant must:

- Retrieve relevant evidence.
- Generate grounded answers.
- Provide source citations.
- Handle insufficient evidence.
- Support follow-up questions.

The system must not present unsupported claims as
verified facts.

### FR-06: Conversation Persistence

Conversations must survive application restarts.

Each conversation must have a stable identifier.

Users must be able to resume previous conversations.

Conversation history and research workflow state must
remain conceptually separate.

### FR-07: Agentic Research

Users must be able to initiate multi-step investigations.

The system must:

1. Interpret the research objective.
2. Generate a research plan.
3. Select appropriate research tools.
4. Retrieve evidence.
5. Assess evidence quality and coverage.
6. Identify information gaps.
7. Perform bounded follow-up research.
8. Synthesize findings.
9. Validate citations.
10. Generate a research report.

Research loops must enforce configurable limits.

### FR-08: Web Research

The assistant must support web search and source retrieval.

Web sources must include:

- URL
- Title, when available
- Retrieval timestamp
- Relevant extracted content
- Source identifier

Retrieved web content is untrusted input.

The assistant must not treat instructions found inside
retrieved documents or web pages as developer instructions.

### FR-09: Research Reports

Research results must support structured output.

A report may include:

- Research question
- Executive summary
- Key findings
- Evidence references
- Citations
- Conflicting evidence
- Limitations
- Unanswered questions
- Suggested follow-up research

Reports must support Markdown export.

Additional export formats can be introduced later.

### FR-10: Citation Verification

Each generated citation must reference an existing
retrieved evidence record.

The system must validate:

- Source identifiers
- Document references
- Page references, where applicable
- Evidence existence
- Claim-to-evidence support

Citation validity and factual correctness are distinct.

Citation existence checks must be deterministic.

Semantic support checks may use model-based evaluation
but must not be treated as infallible.

### FR-11: Streaming

The backend must support streaming research progress.

The CLI should display:

- Current research phase
- Tool execution progress
- Research status
- Final response
- Citations

Use Server-Sent Events where appropriate.

### FR-12: Workflow Persistence

Research workflows must support durable checkpointing.

Workflows should recover from supported interruptions
without losing committed research state.

External side effects must be designed for safe retries.

### FR-13: Human-in-the-Loop

Selected research operations may require approval.

Examples:

- Expensive research operations
- Research plan confirmation
- Sensitive external operations

Approval workflows must support pausing and resuming
execution with persisted state.

---

## 8. LangGraph Design

The research workflow uses explicit typed state.

Conceptual state fields:

```python
class ResearchState(TypedDict):
    question: str
    research_plan: list[str]
    evidence: list[dict]
    findings: list[str]
    research_iteration: int
    report: dict | None
```

This is an illustrative schema, not the final implementation.

Production state models must use appropriate typed
domain structures and reducers.

### Initial Workflow Nodes

- Plan Research
- Retrieve Documents
- Search Web
- Merge Evidence
- Evaluate Coverage
- Refine Research
- Generate Answer
- Verify Citations
- Finalize Report

### Conditional Routing

Workflow transitions depend on explicit state.

Example:

```text
Evaluate Evidence
       |
       v
Enough Evidence?
    /       \
   Yes       No
   |         |
   v         v
Generate   Refine
Report     Research
             |
             v
          Retrieve
```

The workflow must terminate when:

- Sufficient evidence is collected.
- Maximum iterations are reached.
- Budget limits are reached.
- A terminal error occurs.
- The workflow is cancelled.

A research workflow should not rely exclusively on
LLM-generated decisions for operational safety.

---

## 9. Data Architecture

### Core Entities

Initial conceptual entities:

- User
- ResearchProject
- Document
- DocumentChunk
- IngestionJob
- Conversation
- ResearchRun
- Evidence
- ResearchReport

Relationships and constraints will be finalized during
database design.

### Persistence Boundaries

Application database:
Stores durable business records.

Vector index:
Stores searchable representations of document chunks.

Object storage:
Stores original files and generated artifacts.

LangGraph checkpoint store:
Stores graph execution state.

Redis:
Stores ephemeral operational data.

### Data Integrity Requirements

- Stable document IDs
- Stable chunk IDs
- Stable research run IDs
- Referential integrity
- Idempotent ingestion
- Transactional metadata updates
- Explicit document lifecycle states
- Source provenance
- Configurable retention policies

---

## 10. API Requirements

The backend exposes versioned REST endpoints.

Initial proposed endpoints:

```text
GET    /api/v1/health

POST   /api/v1/documents
GET    /api/v1/documents
GET    /api/v1/documents/{document_id}
DELETE /api/v1/documents/{document_id}

POST   /api/v1/search

POST   /api/v1/conversations
GET    /api/v1/conversations/{conversation_id}

POST   /api/v1/research
GET    /api/v1/research/{run_id}
GET    /api/v1/research/{run_id}/events
POST   /api/v1/research/{run_id}/resume
POST   /api/v1/research/{run_id}/cancel

GET    /api/v1/reports/{report_id}
```

These routes are proposed contracts, not implemented APIs.

The exact schemas and route semantics will be defined
during their corresponding implementation phases.

The API must use:

- Pydantic request/response models
- Consistent errors
- Input validation
- OpenAPI documentation
- Authentication and authorization where applicable
- Resource ownership checks
- Appropriate HTTP status codes

---

## 11. Terminal Interface

The primary user interface uses Typer and Rich.

### Proposed Commands

```bash
research ingest ./paper.pdf

research documents list

research documents delete DOCUMENT_ID

research search "transformer attention"

research ask "Explain self-attention"

research investigate "Compare RAG strategies"

research status RUN_ID

research resume RUN_ID

research history

research report RUN_ID
```

Command names are provisional.

### CLI Design Principles

- CLI communicates with FastAPI over HTTP.
- CLI contains presentation logic, not research logic.
- Results are presented using Rich.
- Streaming progress is displayed in the terminal.
- Failures have actionable error messages.
- Commands support machine-readable output when useful.

The CLI and API must share documented contracts.

---

## 12. Reliability Requirements

### Error Handling

Handle:

- LLM provider failures
- API timeouts
- Rate limits
- Invalid model outputs
- Database failures
- Embedding failures
- Document extraction failures
- Corrupted files
- Research tool failures
- Missing evidence
- Workflow interruptions

### Reliability Mechanisms

- Bounded retries
- Exponential backoff
- Request timeouts
- Idempotency keys where appropriate
- Safe background-job retries
- Workflow checkpoints
- Cancellation
- Explicit failure states

Retry behavior must distinguish transient failures
from permanent failures.

---

## 13. Security Requirements

### Application Security

- Secrets stored in environment variables or a secret manager
- No API keys committed to GitHub
- Input validation
- File upload restrictions
- Authentication and authorization
- Resource-level access control
- Rate limiting
- Dependency vulnerability checks

### AI-Specific Security

- Prompt-injection defenses
- Separation of trusted and untrusted content
- Tool permission boundaries
- Output validation
- Restricted file access
- Web-fetch restrictions against SSRF
- Sensitive-data protection
- Limits on autonomous execution

Security boundaries must be enforced in application code,
not only described in prompts.

---

## 14. Observability

### LangSmith

Track:

- LLM calls
- Tool calls
- Agent executions
- LangGraph node execution
- Token usage
- Model latency
- Errors
- Evaluation results

### Application Telemetry

Use structured logging and OpenTelemetry.

Important identifiers:

- request_id
- conversation_id
- research_run_id
- document_id
- trace_id

Observability must make it possible to understand:

1. What the system attempted.
2. Which tools and models it called.
3. Which evidence it retrieved.
4. Why it followed a particular workflow path.
5. Where failures occurred.
6. What an investigation cost.

Do not log secrets or sensitive document contents by default.

---

## 15. Testing and Evaluation

### Unit Tests

Cover:

- Document processing
- Chunk generation
- Metadata handling
- Retrieval fusion
- Citation validation
- Graph routing
- Domain logic

### Integration Tests

Cover:

- PostgreSQL
- pgvector
- Redis
- Object storage
- FastAPI
- Background jobs
- Workflow persistence

### AI Evaluations

Evaluate:

- Retrieval recall
- Retrieval precision
- Reranking effectiveness
- Citation correctness
- Answer groundedness
- Research completeness
- Tool-use correctness
- Workflow termination
- Cost and latency

Use representative datasets rather than relying
exclusively on manually inspected responses.

### Evaluation Philosophy

Every advanced retrieval strategy must demonstrate
measurable value over a simpler baseline.

Do not assume that adding more agents, retrieval steps,
or model calls automatically improves quality.

---

## 16. Performance and Cost

The system must track:

- LLM token consumption
- Embedding costs
- Retrieval latency
- Reranking latency
- Research duration
- Tool call counts
- Background job duration

Optimization strategies may include:

- Embedding reuse
- Batched embedding requests
- Caching
- Efficient database indexing
- Context budgeting
- Model routing
- Parallel independent research operations

Optimize based on observed bottlenecks.

---

## 17. Repository Structure

Proposed initial structure:

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
│   │   │   ├── agents/
│   │   │   ├── nodes/
│   │   │   ├── state.py
│   │   │   └── graph.py
│   │   ├── services/
│   │   ├── workers/
│   │   └── main.py
│   ├── alembic/
│   ├── tests/
│   └── pyproject.toml
├── cli/
│   ├── evidentia_cli/
│   └── pyproject.toml
├── infra/
│   └── compose.yaml
├── docs/
│   ├── architecture/
│   └── adr/
├── evals/
├── .github/
│   └── workflows/
├── .env.example
├── SPEC.md
└── README.md
```

The final repository structure may evolve through documented
architecture decisions.

Do not create speculative abstractions before their first
concrete use case.

---

## 18. Implementation Roadmap

### Phase 1 — Backend Foundation

Implement:

- Project scaffolding
- uv configuration
- FastAPI application
- Environment configuration
- PostgreSQL integration
- SQLAlchemy
- Alembic
- Docker Compose
- Health endpoint
- Minimal Typer CLI
- Initial automated tests

Deliverable:

A CLI that communicates with a running FastAPI backend.

### Phase 2 — Document Ingestion

Implement:

- PDF uploads
- Document storage
- Text extraction
- Chunking
- Metadata
- Embeddings
- pgvector indexing
- Background ingestion
- Ingestion status tracking

Deliverable:

Upload and index real research papers.

### Phase 3 — Advanced RAG

Implement:

- Semantic search
- Keyword search
- Hybrid retrieval
- Rank fusion
- Reranking
- Query rewriting
- Grounded Q&A
- Citation metadata
- Retrieval evaluations

Deliverable:

A measurable, citation-aware research Q&A engine.

### Phase 4 — LangGraph Research Workflow

Implement:

- Typed graph state
- Research planning
- Workflow nodes
- Conditional routing
- Iterative retrieval
- Checkpointing
- Retry and termination controls
- Structured research reports

Deliverable:

A stateful, multi-step research workflow.

### Phase 5 — Agentic Web Research

Implement:

- Research tools
- Web search
- Source retrieval
- Research agents
- Parallel evidence gathering
- Source reconciliation
- Evidence validation

Deliverable:

Research combining local documents and web sources.

### Phase 6 — Memory and Human Oversight

Implement:

- Persistent conversations
- Follow-up question handling
- Research history
- Human approval
- Workflow interruption
- Workflow resumption

Deliverable:

Recoverable research sessions with human oversight.

### Phase 7 — Advanced CLI Experience

Implement:

- Streaming output
- Interactive research sessions
- Research history
- Citation display
- Progress visualization
- Markdown report export

Deliverable:

A complete terminal-based research assistant.

### Phase 8 — Production Engineering

Implement:

- Authentication
- Authorization
- Security hardening
- Structured logging
- LangSmith tracing
- Evaluation datasets
- Cost tracking
- Reliability controls
- CI
- Deployment configuration

Deliverable:

A tested, monitored, deployable application.

---

## 19. Development Standards

### Code Quality

- Type annotations for public interfaces.
- Pydantic for external data validation.
- Explicit error handling.
- Descriptive names.
- Small, cohesive functions.
- Clear module boundaries.
- No unnecessary abstraction.
- No hardcoded secrets.
- No hidden provider dependencies.

### Dependency Management

Use uv lockfiles.

Pin compatible versions and commit lockfiles.

Check current official documentation before introducing
framework-specific APIs.

Do not blindly copy syntax from older tutorials.

### Database Changes

All schema changes must use Alembic migrations.

Do not modify production database schemas manually.

### Testing

New functionality must include appropriate tests.

Bug fixes should add regression tests when practical.

### Documentation

Document architectural decisions that materially affect:

- Data flow
- Persistence
- Reliability
- Security
- Performance
- Dependency choices
- Operational behavior

---

## 20. AI-Assisted Development Rules

When collaborating with an AI programming assistant:

1. Treat GitHub as the code SSOT.
2. Inspect existing code before suggesting changes.
3. Use official, version-appropriate documentation.
4. Explain the design before complex implementations.
5. Implement changes in logical increments.
6. Explain important execution paths.
7. Identify failure modes and trade-offs.
8. Prefer simple solutions that meet requirements.
9. Avoid deprecated LangChain and LangGraph patterns.
10. Do not introduce unrelated technologies.
11. Do not claim untested functionality works.
12. Distinguish proposals from implemented features.
13. Maintain compatibility with existing modules.
14. Update tests when behavior changes.
15. Keep implementation aligned with this specification.

### Teaching Requirements

For significant implementation steps, explain:

- Purpose
- Architecture
- Execution flow
- State changes
- Data flow
- Failure handling
- Engineering trade-offs

Avoid unnecessary Python or backend fundamentals.

Prioritize AI engineering concepts and production reasoning.

---

## 21. Definition of Done

A feature is complete when:

1. Its expected behavior is implemented.
2. Its API or CLI contract is defined.
3. Relevant tests pass.
4. Errors are handled appropriately.
5. Persistent state is managed correctly.
6. Security considerations are addressed.
7. Observability exists where appropriate.
8. Documentation reflects the implementation.
9. No known critical regression is introduced.
10. Changes are committed to the GitHub repository.

A tutorial demonstration alone does not satisfy
the definition of done.

---

## 22. Final Project Acceptance Criteria

Evidentia is complete when a user can:

1. Start the application through documented commands.
2. Ingest real research PDFs.
3. Search indexed documents.
4. Ask questions with verifiable citations.
5. Compare evidence across multiple documents.
6. Initiate multi-step research investigations.
7. Combine document evidence with web research.
8. Monitor research progress from the terminal.
9. Resume persisted research sessions.
10. Generate structured research reports.
11. Inspect research sources and limitations.
12. Recover appropriately from supported failures.

The engineering implementation must additionally include:

- Automated tests
- AI evaluations
- Persistent storage
- Workflow checkpointing
- Security controls
- Observability
- Cost management
- Reproducible deployment

---

## 23. Guiding Principle

Evidentia must prioritize evidence quality,
reliability, and explainability over agent complexity.

Build reliable retrieval first.

Add controlled research workflows second.

Introduce autonomous tool use where it provides
measurable value.

Optimize and scale based on evidence.

The objective is not to create the largest agent system.

The objective is to understand and implement the
engineering principles behind a reliable,
production-oriented AI research platform.
