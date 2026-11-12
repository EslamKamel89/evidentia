# Evidentia — Course Progress Tracker

**Repository:** https://github.com/EslamKamel89/evidentia
**Course Plan:** [course_plan.md](course_plan.md)
**Project Specification:** [SPEC.md](../SPEC.md)

## Progress Overview

| Metric           | Value |
| ---------------- | ----- |
| Total Sections   | 6     |
| Total Lessons    | 15    |
| Completed        | 1     |
| In Progress      | 0     |
| Not Started      | 14    |
| Overall Progress | 6.7%  |

## Lesson Progress

| #   | Section                                     | Lesson                                      | Status      | Completion Date |
| --- | ------------------------------------------- | ------------------------------------------- | ----------- | --------------- |
| 01  | Application Foundation                      | Project Architecture & Infrastructure       | Completed   | 2026-11-12      |
| 02  | Application Foundation                      | Terminal CLI & API Integration              | Not Started | —               |
| 03  | Document Intelligence & RAG                 | Production Document Ingestion               | Not Started | —               |
| 04  | Document Intelligence & RAG                 | Advanced Retrieval Engine                   | Not Started | —               |
| 05  | Document Intelligence & RAG                 | Evidence-Grounded RAG & Structured Answers  | Not Started | —               |
| 06  | LangGraph & Agentic Research                | LangGraph Research Orchestrator             | Not Started | —               |
| 07  | LangGraph & Agentic Research                | Tool-Calling Agents & Web Research          | Not Started | —               |
| 08  | LangGraph & Agentic Research                | Research Synthesis & Verification           | Not Started | —               |
| 09  | Persistence, Memory & Interactive Workflows | Persistent Memory & Durable Execution       | Not Started | —               |
| 10  | Persistence, Memory & Interactive Workflows | Streaming Research & CLI Experience         | Not Started | —               |
| 11  | Production AI Engineering                   | Reliability, Security & Guardrails          | Not Started | —               |
| 12  | Production AI Engineering                   | LangSmith Observability & Cost Optimization | Not Started | —               |
| 13  | Production AI Engineering                   | AI Testing & Evaluation                     | Not Started | —               |
| 14  | Deployment & Final Integration              | Containerization, CI & Deployment           | Not Started | —               |
| 15  | Deployment & Final Integration              | End-to-End Research System Validation       | Not Started | —               |

---

## Lesson Notes

Notes document implementation decisions, key concepts,
problems encountered, and remaining work.

### Lesson 01 — Project Architecture & Infrastructure

**Completion Date:** 2026-11-12

**Status:** Completed — Initial API checkpoint verified;
remaining infrastructure work outstanding.

#### Implemented

- Initialized the backend as an installable Python package.
- Configured Python 3.12 and uv.
- Established the `src/evidentia_backend` package layout.
- Installed FastAPI, Uvicorn, and Pydantic Settings.
- Configured development dependencies.
- Implemented the FastAPI application factory.
- Created the `/api/v1/health` endpoint.
- Implemented the first API test using pytest.
- Introduced reusable pytest fixtures.
- Updated VS Code interpreter and Python import settings.
- Configured Ruff formatting and import organization.

#### Key Concepts

- Modular monolith architecture.
- Application factories and application lifecycle.
- Python package structure and import resolution.
- HTTP request handling with FastAPI.
- Test isolation using pytest fixtures.
- TestClient context management and lifespan handling.
- Dependency separation between application and tests.

#### Verification

- [x] FastAPI application implemented.
- [x] Health endpoint implemented.
- [x] Health endpoint test passed.
- [x] Reusable pytest fixtures introduced.
- [ ] PostgreSQL connection verified.
- [ ] SQLAlchemy configured.
- [ ] Alembic migrations verified.
- [ ] Redis connection verified.
- [ ] Docker Compose infrastructure verified.

#### Remaining Infrastructure Work

- Implement environment configuration with Pydantic Settings.
- Configure PostgreSQL and SQLAlchemy.
- Implement database session management.
- Initialize Alembic migrations.
- Configure Redis.
- Create Docker Compose infrastructure.
- Add infrastructure-aware health checks.

#### Notes

The initial backend application and API testing foundation
are working.

The remaining infrastructure requirements must be completed
before features depending on persistent storage or background
processing are introduced.

---

### Lesson 02 — Terminal CLI & API Integration

_No notes yet._

### Lesson 03 — Production Document Ingestion

_No notes yet._

### Lesson 04 — Advanced Retrieval Engine

_No notes yet._

### Lesson 05 — Evidence-Grounded RAG & Structured Answers

_No notes yet._

### Lesson 06 — LangGraph Research Orchestrator

_No notes yet._

### Lesson 07 — Tool-Calling Agents & Web Research

_No notes yet._

### Lesson 08 — Research Synthesis & Verification

_No notes yet._

### Lesson 09 — Persistent Memory & Durable Execution

_No notes yet._

### Lesson 10 — Streaming Research & CLI Experience

_No notes yet._

### Lesson 11 — Reliability, Security & Guardrails

_No notes yet._

### Lesson 12 — LangSmith Observability & Cost Optimization

_No notes yet._

### Lesson 13 — AI Testing & Evaluation

_No notes yet._

### Lesson 14 — Containerization, CI & Deployment

_No notes yet._

### Lesson 15 — End-to-End Research System Validation

_No notes yet._

---

## Tracking Rules

1. **Allowed statuses:** `Not Started`, `In Progress`,
   `Completed`, `Blocked`.
2. Use `YYYY-MM-DD` for completion dates.
3. Mark lessons completed only after verifying deliverables.
4. Leave completion dates as `—` for unfinished lessons.
5. Update the progress overview when statuses change.
6. Append notes under the corresponding lesson.
7. Preserve previous notes when revisiting lessons.
8. Reference GitHub commits or pull requests when useful.
9. GitHub is the single source of truth for progress.
10. Keep this file synchronized with `course_plan.md`.
