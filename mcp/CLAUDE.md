# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

## Essential Commands

**Development:**

```bash
# Install dependencies
uv sync

# Build embeddings database (required before first run)
uv run build-embeddings

# Run MCP server locally
uv run serve

# Lint code
uv run ruff check

# Type check code
uv run mypy .

# Build container
podman build -t managed-notifications-search .

# Run container
podman run -p 8000:8000 managed-notifications-search
```

## Architecture Overview

This is an MCP (Model Context Protocol) server that provides semantic search
over OpenShift service notification logs using vector embeddings. The system
has two main phases:

### Build Phase (Offline)

- **Input**: JSON notification files from `managed-notifications/` directory
- **Processing**: `scripts/build_embeddings.py` extracts searchable text,
  creates embeddings via sentence-transformers, stores in ChromaDB
- **Output**: Persistent vector database in `chroma_db/` directory
- **Key Feature**: Extracts variable placeholders (e.g., `${TIME}`, `${POD}`)
  from notification templates

### Runtime Phase (Online)

- **Server**: `main.py` implements FastMCP server with HTTP transport
- **Search**: Uses same embedding model to vectorize queries, performs
  similarity search in ChromaDB
- **Tools**: Exposes `search_service_logs` and `get_database_stats` MCP tools

### Data Flow

1. Problem statement → Query embedding → Vector similarity search →
   Ranked results
2. Results include notification JSON, metadata (folder, severity, variables),
   and similarity scores

## Critical Implementation Details

**Variable Handling**: Service notifications contain template variables like
`${NAMESPACE}`, `${REASON}` that must be interpolated. The system:

- Extracts variables using regex during embedding creation
- Stores them as JSON strings in ChromaDB metadata (scalar value requirement)
- Returns parsed variable lists to guide LLM interpolation workflow

**Container Architecture**: Multi-stage build separates embedding creation
(expensive, cached) from runtime (lightweight). Only rebuilds embeddings when
notification files or embedding script change.

**Project Scripts**: Uses uv project scripts defined in `pyproject.toml`:

- `serve = "main:main"`
- `build-embeddings = "scripts.build_embeddings:main"`

**MCP Configuration**: `mcp-config.json` provides ready-to-use HTTP transport
config for MCP clients connecting to `localhost:8000/mcp`.

## Environment Variables

- `EMBEDDING_MODEL`: Override default sentence transformer model
  (default: "all-MiniLM-L6-v2")
- `HOST`: Server bind address (default: "127.0.0.1", container uses "0.0.0.0")
- `PORT`: Server port (default: "8000")

## Database Dependencies

The MCP server requires the ChromaDB database to exist before startup. Always
run `uv run build-embeddings` before `uv run serve` in fresh environments. The
embeddings script includes a test search for "missing or insufficient
permissions" to validate the database.
