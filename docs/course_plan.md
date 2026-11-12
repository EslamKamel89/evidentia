# Evidentia — Project-Based AI Engineering Course

**Project:** Evidentia — Agentic AI Research Assistant  
**Repository:** https://github.com/EslamKamel89/evidentia  
**Specification:** [SPEC.md](../SPEC.md)  
**Status:** Approved — Not Started

## Course Overview

Build a production-oriented AI research assistant using
LangChain, LangGraph, advanced RAG, FastAPI, and Python.

The course follows the actual engineering lifecycle:

**Infrastructure → Document Ingestion → Advanced RAG →
Agentic Research → Persistent Workflows → Production**

The goal is to understand how reliable AI systems are
designed, implemented, tested, and deployed.

### Course Structure

| Section   | Topic                                       | Lessons |
| --------- | ------------------------------------------- | ------- |
| 1         | Application Foundation                      | 2       |
| 2         | Document Intelligence & RAG                 | 3       |
| 3         | LangGraph & Agentic Research                | 3       |
| 4         | Persistence, Memory & Interactive Workflows | 2       |
| 5         | Production AI Engineering                   | 3       |
| 6         | Deployment & Final Integration              | 2       |
| **Total** | **6 Sections**                              | **15**  |

### Learning Method

Each lesson follows this process:

1. **Problem:** Understand the engineering problem.
2. **Architecture:** Understand the design and trade-offs.
3. **Implementation:** Build the feature incrementally.
4. **Execution:** Trace data flow, state, and runtime behavior.
5. **Testing:** Verify correctness and failure handling.
6. **Deliverable:** Produce working, testable functionality.

Every lesson builds on the existing Evidentia codebase.

The GitHub repository is the single source of truth
for implementation.

---

# Section 1 — Application Foundation

**Goal:** Establish the backend architecture and
CLI-to-API communication.

## Lesson 01 — Project Architecture & Infrastructure

### Concepts

- Modular monolith architecture
- Application boundaries
- Dependency management with uv
- Environment-based configuration
- Dependency injection
- Database integration
- Database migrations
- Containerized development

### Implementation

- Initialize the Python project.
- Configure uv and development dependencies.
- Establish the backend package structure.
- Create the FastAPI application.
- Implement configuration using Pydantic Settings.
- Configure PostgreSQL and SQLAlchemy 2.
- Initialize Alembic migrations.
- Configure Redis.
- Create Docker Compose infrastructure.
- Add Ruff, Pyright, and pytest.
- Implement a health endpoint.

### Deliverable

A reproducible backend that:

- Starts successfully.
- Connects to PostgreSQL.
- Applies database migrations.
- Exposes a working health endpoint.
- Runs with Docker Compose.

**Verification:** Start the infrastructure and execute
the health endpoint and initial tests successfully.

---

## Lesson 02 — Terminal CLI & API Integration

### Concepts

- CLI architecture
- HTTP client design
- API contracts
- Request/response validation
- Separation of presentation and application logic
- Error propagation

### Implementation

- Initialize the Typer CLI.
- Configure Rich output formatting.
- Implement an HTTPX API client.
- Add API connection configuration.
- Implement CLI error handling.
- Create health and information commands.
- Test CLI-to-API communication.

### Deliverable

Working terminal commands:

```bash
evidentia health
evidentia info
```

**Verification:** Both commands communicate with
FastAPI and display formatted responses.

---

# Section 2 — Document Intelligence & RAG

**Goal:** Transform research documents into searchable,
evidence-grounded knowledge.

## Lesson 03 — Production Document Ingestion

### Concepts

- Document ingestion architecture
- File storage and metadata
- PDF text extraction
- Chunking strategies
- Embedding generation
- Vector indexing
- Background job processing
- Idempotency and ingestion lifecycle

### Implementation

- Implement PDF upload endpoints.
- Configure S3-compatible object storage.
- Extract text using PyMuPDF.
- Preserve page-level metadata.
- Implement document chunking.
- Generate OpenAI embeddings.
- Store vectors using pgvector.
- Implement Dramatiq ingestion workers.
- Track ingestion status.
- Handle duplicate ingestion.
- Implement document listing and deletion.

### Deliverable

Working commands:

```bash
evidentia ingest ./paper.pdf
evidentia documents list
```

**Verification:** A real PDF is stored, processed,
indexed, and available for retrieval.

---

## Lesson 04 — Advanced Retrieval Engine

### Concepts

- Semantic similarity search
- PostgreSQL full-text search
- Hybrid retrieval
- Reciprocal Rank Fusion (RRF)
- Metadata filtering
- Query rewriting and expansion
- Cross-encoder reranking
- Retrieval quality measurement

### Implementation

- Implement semantic retrieval.
- Implement keyword retrieval.
- Combine retrieval results using RRF.
- Add metadata filters.
- Implement query expansion.
- Add reranking.
- Return source metadata and relevance information.
- Create retrieval comparison tests.

### Deliverable

Working command:

```bash
evidentia search "transformer attention"
```

The command returns ranked document passages
with source metadata.

**Verification:** Compare basic semantic retrieval
against hybrid retrieval using a reproducible
test dataset.

---

## Lesson 05 — Evidence-Grounded RAG & Structured Answers

### Concepts

- Retrieval-augmented generation
- Context construction
- Prompt grounding
- LangChain v1 model integration
- Pydantic structured outputs
- Evidence provenance
- Citation validation
- Insufficient-evidence handling

### Implementation

- Build the retrieval-generation pipeline.
- Construct prompts using retrieved evidence.
- Implement structured research responses.
- Assign stable evidence identifiers.
- Connect citations to retrieved passages.
- Validate citation references.
- Handle questions without sufficient evidence.
- Test grounded answer generation.

### Deliverable

Working command:

```bash
evidentia ask "Explain self-attention"
```

The assistant generates an answer with citations
linked to actual document passages and pages.

**Verification:** Every generated citation resolves
to an existing evidence record, and unsupported
questions are handled explicitly.

---

# Section 3 — LangGraph & Agentic Research

**Goal:** Transform a fixed RAG pipeline into an
adaptive, stateful research system.

## Lesson 06 — LangGraph Research Orchestrator

### Concepts

- StateGraph
- Typed graph state
- Nodes and edges
- State reducers
- Conditional routing
- Research planning
- Evidence assessment
- Iterative workflows
- Bounded execution

### Implementation

- Define the research state schema.
- Implement a research planning node.
- Implement document retrieval nodes.
- Add evidence evaluation.
- Implement conditional routing.
- Add research refinement loops.
- Enforce maximum research iterations.
- Generate an initial research report.
- Test graph state transitions.

### Deliverable

A working LangGraph workflow that:

1. Receives a research question.
2. Creates a research plan.
3. Retrieves local evidence.
4. Evaluates evidence coverage.
5. Performs bounded follow-up retrieval.
6. Produces a research report.

**Verification:** The graph follows expected
routes and terminates under configured limits.

---

## Lesson 07 — Tool-Calling Agents & Web Research

### Concepts

- LangChain create_agent
- Tool calling
- Agent versus workflow responsibilities
- Tool schemas
- External research APIs
- Parallel evidence gathering
- Tool execution safety
- Source provenance

### Implementation

- Define research tools.
- Implement a LangChain tool-calling agent.
- Integrate Tavily search.
- Implement web content retrieval.
- Normalize web evidence.
- Connect research tools to LangGraph.
- Support parallel independent research operations.
- Handle tool failures and timeouts.

### Deliverable

The research workflow can:

- Search indexed documents.
- Search external web sources.
- Select appropriate research tools.
- Collect evidence from both sources.

**Verification:** A research investigation
successfully combines local and web evidence.

---

## Lesson 08 — Research Synthesis & Verification

### Concepts

- Evidence aggregation
- Conflicting evidence
- Research gap analysis
- Grounded synthesis
- Citation verification
- Structured research reports
- Research limitations

### Implementation

- Merge document and web evidence.
- Deduplicate evidence records.
- Identify conflicting findings.
- Evaluate remaining research gaps.
- Generate structured research reports.
- Validate citation references.
- Check claim-to-evidence support.
- Implement Markdown report export.

### Deliverable

Working command:

```bash
evidentia investigate "Compare RAG strategies"
```

The command generates a multi-source report containing:

- Research summary
- Key findings
- Supporting evidence
- Citations
- Conflicting evidence
- Limitations
- Follow-up questions

**Verification:** Reports reference actual evidence
and identify unsupported or conflicting findings.

---

# Section 4 — Persistence, Memory & Interactive Workflows

**Goal:** Make research durable, resumable, and
observable from the terminal.

## Lesson 09 — Persistent Memory & Durable Execution

### Concepts

- Conversation memory versus workflow state
- LangGraph checkpointing
- Thread identifiers
- Persistent execution
- Workflow interruption
- Human-in-the-loop
- Safe resumption
- Idempotent side effects

### Implementation

- Configure PostgreSQL-backed checkpointing.
- Persist conversation records.
- Implement conversation isolation.
- Support contextual follow-up questions.
- Implement workflow interrupts.
- Add human approval.
- Implement workflow resumption.
- Test recovery after application restart.

### Deliverable

Research sessions that:

- Survive application restarts.
- Preserve conversation context.
- Support follow-up questions.
- Pause for human approval.
- Resume from persisted checkpoints.

**Verification:** Stop and restart the application,
then resume an existing research session.

---

## Lesson 10 — Streaming Research & CLI Experience

### Concepts

- Server-Sent Events
- LangGraph event streaming
- Async event consumption
- Research progress tracking
- Cancellation
- Terminal presentation

### Implementation

- Implement FastAPI streaming endpoints.
- Stream LangGraph execution events.
- Consume SSE using HTTPX.
- Display progress using Rich.
- Show research phases and tool activity.
- Implement research cancellation.
- Add research history commands.
- Display saved reports and citations.

### Deliverable

An interactive terminal research experience
that displays:

- Current research phase
- Tool execution
- Progress updates
- Research results
- Citations
- Final reports

**Verification:** Run an investigation and observe
live progress from the CLI through completion.

---

# Section 5 — Production AI Engineering

**Goal:** Establish reliability, security, and
measurable AI quality.

## Lesson 11 — Reliability, Security & Guardrails

### Concepts

- Transient versus permanent failures
- Retry strategies
- Timeouts
- Idempotency
- Execution budgets
- Authentication and authorization
- Prompt injection
- SSRF protection
- Tool permission boundaries

### Implementation

- Implement bounded retries.
- Configure request and tool timeouts.
- Enforce research iteration limits.
- Implement token and cost budgets.
- Add authentication.
- Enforce resource ownership.
- Validate uploaded files.
- Protect external web requests.
- Add prompt-injection defenses.
- Test failure and abuse scenarios.

### Deliverable

A research system that handles controlled
failure scenarios and enforces security boundaries.

**Verification:** Automated tests demonstrate
that configured limits and access controls
are enforced.

---

## Lesson 12 — LangSmith Observability & Cost Optimization

### Concepts

- Distributed tracing
- LLM observability
- LangSmith
- Structured logging
- OpenTelemetry
- Token accounting
- Cost monitoring
- Caching
- Model selection

### Implementation

- Integrate LangSmith tracing.
- Trace LangGraph execution.
- Track LLM and tool calls.
- Add structured application logs.
- Configure OpenTelemetry.
- Track token usage and estimated costs.
- Implement appropriate caching.
- Configure model selection.
- Monitor latency and failures.

### Deliverable

A complete research investigation can be
inspected through traces and logs.

**Verification:** Identify model calls, tool calls,
execution paths, latency, errors, and estimated
cost for a specific research run.

---

## Lesson 13 — AI Testing & Evaluation

### Concepts

- AI testing pyramid
- Deterministic versus probabilistic testing
- Retrieval evaluation
- Groundedness
- Citation accuracy
- LLM-as-judge
- Regression datasets
- Workflow testing

### Implementation

- Implement unit tests for research components.
- Add database integration tests.
- Test LangGraph routing and state.
- Create representative research datasets.
- Benchmark retrieval strategies.
- Evaluate answer groundedness.
- Measure citation correctness.
- Add research workflow regression tests.
- Integrate LangSmith evaluations.

### Deliverable

A reproducible evaluation suite measuring:

- Retrieval quality
- Answer groundedness
- Citation correctness
- Workflow correctness
- Research reliability

**Verification:** Run the evaluation suite
and compare results against established baselines.

---

# Section 6 — Deployment & Final Integration

**Goal:** Ship and validate the complete system.

## Lesson 14 — Containerization, CI & Deployment

### Concepts

- Production containerization
- Multi-service deployment
- Environment configuration
- Database migrations
- Continuous integration
- Deployment reproducibility
- Service health and readiness

### Implementation

- Finalize backend Docker images.
- Configure CLI packaging.
- Finalize Docker Compose services.
- Manage environment-specific settings.
- Configure production database migrations.
- Create GitHub Actions workflows.
- Run linting, type checking, and tests in CI.
- Prepare deployment configuration.
- Document deployment procedures.

### Deliverable

A reproducibly deployable Evidentia application
with automated CI quality checks.

**Verification:** Build and start the complete
application from documented deployment instructions.

---

## Lesson 15 — End-to-End Research System Validation

### Concepts

- End-to-end system validation
- Integration boundaries
- Failure recovery
- Performance verification
- Production readiness
- Technical documentation

### Implementation

- Test document ingestion end to end.
- Validate hybrid retrieval.
- Execute agentic research workflows.
- Test web research integration.
- Verify persistent sessions.
- Test interruption and resumption.
- Validate citation generation.
- Test streaming and cancellation.
- Generate and inspect research reports.
- Fix integration failures.
- Document known limitations.
- Prepare the final release.

### Deliverable

A tested and documented Evidentia release
satisfying the project specification.

**Verification:** Execute the full acceptance
test scenario successfully.

---

# Final Acceptance Scenario

The completed application must support the following
end-to-end workflow:

### 1. Start the Application

Start Evidentia using documented commands.

Verify backend, database, cache, and worker health.

### 2. Ingest Research Papers

```bash
evidentia ingest ./papers/paper1.pdf
evidentia ingest ./papers/paper2.pdf
```

Verify successful document indexing.

### 3. Search Documents

```bash
evidentia search "retrieval augmented generation"
```

Verify ranked results with source metadata.

### 4. Ask Grounded Questions

```bash
evidentia ask "What are the limitations of RAG?"
```

Verify answers include valid citations.

### 5. Perform Agentic Research

```bash
evidentia investigate \
  "Compare modern RAG retrieval strategies"
```

Verify that the system:

- Plans research.
- Searches relevant sources.
- Collects evidence.
- Identifies information gaps.
- Performs bounded follow-up research.
- Synthesizes findings.
- Validates citations.
- Generates a structured report.

### 6. Validate Persistence

Restart the application and resume
a previously persisted research session.

### 7. Inspect Observability

Inspect execution traces, tool calls,
model usage, latency, and costs.

### 8. Run Evaluations

Execute automated tests and AI evaluations.

Verify the results against established baselines.

---

# Course Completion Criteria

The course is complete when:

- [ ] All 15 lesson deliverables are implemented.
- [ ] All required application features work.
- [ ] The CLI communicates correctly with FastAPI.
- [ ] Document ingestion is persistent and reliable.
- [ ] Advanced retrieval is implemented and evaluated.
- [ ] Research workflows use LangGraph.
- [ ] Research agents use supported LangChain APIs.
- [ ] Citations reference verifiable evidence.
- [ ] Conversations and workflows persist.
- [ ] Research progress streams to the terminal.
- [ ] Security and reliability controls are enforced.
- [ ] Observability and cost tracking are operational.
- [ ] Automated tests and evaluations pass.
- [ ] Deployment is reproducible.
- [ ] The GitHub repository contains current documentation.
- [ ] Evidentia satisfies the acceptance criteria in SPEC.md.

---

# Engineering Rules

1. GitHub is the single source of truth for code.
2. Every lesson builds on the existing repository.
3. Verify current LangChain and LangGraph APIs.
4. Prefer supported, non-deprecated APIs.
5. Explain architectural decisions before implementation.
6. Trace execution and state changes.
7. Introduce abstractions only when justified.
8. Include appropriate tests with each feature.
9. Keep CLI, API, and research logic separated.
10. Measure AI quality rather than assuming correctness.
11. Maintain documentation alongside implementation.
12. Complete and verify each lesson deliverable before
    proceeding to the next lesson.

---

# Progress Tracker

| Lesson | Topic                                       | Status      |
| ------ | ------------------------------------------- | ----------- |
| 01     | Project Architecture & Infrastructure       | Not Started |
| 02     | Terminal CLI & API Integration              | Not Started |
| 03     | Production Document Ingestion               | Not Started |
| 04     | Advanced Retrieval Engine                   | Not Started |
| 05     | Evidence-Grounded RAG & Structured Answers  | Not Started |
| 06     | LangGraph Research Orchestrator             | Not Started |
| 07     | Tool-Calling Agents & Web Research          | Not Started |
| 08     | Research Synthesis & Verification           | Not Started |
| 09     | Persistent Memory & Durable Execution       | Not Started |
| 10     | Streaming Research & CLI Experience         | Not Started |
| 11     | Reliability, Security & Guardrails          | Not Started |
| 12     | LangSmith Observability & Cost Optimization | Not Started |
| 13     | AI Testing & Evaluation                     | Not Started |
| 14     | Containerization, CI & Deployment           | Not Started |
| 15     | End-to-End Research System Validation       | Not Started |

**Total Progress: 0 / 15 Lessons**

Update lesson status only after the corresponding
deliverable has been implemented and verified
in the GitHub repository.
