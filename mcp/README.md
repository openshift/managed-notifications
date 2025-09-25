# Managed Notifications Search MCP Server

An MCP (Model Context Protocol) server that enables AI agents to search through
OpenShift service notification logs using semantic search powered by ChromaDB and
sentence transformers.

## Overview

This server provides semantic search capabilities over OpenShift service
notification JSON files, allowing AI agents to find relevant notifications based
on problem descriptions. The system uses vector embeddings to enable semantic
matching rather than just keyword search.

## Features

- **Semantic Search**: Find notifications based on problem descriptions using
  vector similarity
- **Metadata Enrichment**: Results include folder categories (hcp, osd, rosa,
  etc.), severity levels, and full notification data
- **Efficient Container Deployment**: Multi-stage Docker build with optimized
  layering for embedding regeneration
- **Database Statistics**: Get insights into available notifications and categories

## Installation

### Prerequisites

- Python 3.13+
- uv (Python package manager)
- Git
- Podman or Docker (for containerized deployment)

### Local Development

1. **Clone and setup the repository:**

   ```bash
   git clone <repository-url>
   cd managed-notifications
   ```

2. **Install dependencies:**

   ```bash
   uv sync
   ```

3. **Build the embeddings database:**

   ```bash
   uv run build-embeddings
   ```

4. **Run the MCP server:**

   ```bash
   uv run serve
   ```

### Container Deployment

1. **Build the container:**

   ```bash
   podman build -t managed-notifications-search .
   ```

2. **Run the container:**

   ```bash
   podman run -p 8000:8000 managed-notifications-search
   ```

### MCP Client Configuration

To connect to the server from an MCP client, use the provided configuration file:

**File: `mcp-config.json`**

```json
{
  "mcpServers": {
    "service-logs": {
      "type": "http",
      "url": "http://localhost:8000/mcp",
      "auth": {}
    }
  }
}
```

This configuration enables MCP clients (like Claude Desktop) to connect to the
running server on localhost port 8000.

## Usage

The server provides two main MCP tools:

### `search_service_logs`

Search for notifications matching a problem statement.

**Parameters:**

- `problem_statement` (required): Description of the issue to search for
- `max_results` (optional, default: 5): Maximum number of results to return

**Example:**

```python
# Search for pod scheduling issues
results = search_service_logs(
    problem_statement="pods stuck in pending state unable to schedule",
    max_results=3
)
```

**Important Note on Variable Interpolation:**
Many service notifications contain variable placeholders like `${TIME}`,
`${REASON}`, `${POD}`, `${NAMESPACE}` that need to be replaced with actual values.
When using this tool:

1. **Check the `variables` field** in each result to see what variables need interpolation
2. **Ask users for specific values** for each variable when presenting a notification
3. **Help interpolate variables** into the notification text before sending to customers

Common variables include:

- `${TIME}`: Timestamp when the issue occurred
- `${REASON}`: Specific reason for the failure  
- `${POD}`: Name of the affected pod
- `${NAMESPACE}`: Kubernetes namespace
- `${CLUSTER_ID}`: Cluster identifier
- `${NUM_OF_WORKERS}`: Number of worker nodes

### `get_database_stats`

Get statistics about the notification database.

**Returns:**

- Total number of notifications
- Available folder categories
- Severity levels
- Service names
- Database path

## Architecture

### Components

1. **Embedding Script** (`scripts/build_embeddings.py`):
   - Processes all JSON files in the managed-notifications directory
   - Extracts searchable text from notification fields
   - Creates vector embeddings using sentence-transformers
   - Stores embeddings in ChromaDB with metadata

2. **MCP Server** (`main.py`):
   - FastMCP-based server with search tools
   - Loads pre-built ChromaDB database on startup
   - Provides semantic search and database statistics

3. **Container Configuration**:
   - Multi-stage build separating embedding creation from runtime
   - Optimized layering to minimize rebuilds
   - Non-root user for security

### Data Flow

1. **Build Phase**: JSON files � Text extraction � Vector embeddings �
   ChromaDB
2. **Runtime Phase**: Problem statement � Query embedding � Similarity search
   � Formatted results

## Notification Categories

The system organizes notifications by folder structure:

- **hcp**: Hosted Control Plane notifications
- **osd**: OpenShift Dedicated notifications  
- **rosa**: Red Hat OpenShift Service on AWS notifications
- **cluster**: General cluster notifications
- **ocm**: OpenShift Cluster Manager notifications

## Development

### Project Structure

```text
├── main.py                    # MCP server implementation
├── scripts/
│   └── build_embeddings.py   # Embedding creation script
├── managed-notifications/     # Directory with notification JSONs
├── Containerfile             # Multi-stage container build
├── .containerignore          # Container build exclusions
└── pyproject.toml            # Python dependencies
```

### Embedding Model

The system uses the `all-MiniLM-L6-v2` sentence transformer model by default.
You can override this by setting the `EMBEDDING_MODEL` environment variable in
the embedding script.

### Database Structure

Each notification is stored with:

- **Document**: Concatenated searchable text (summary, description, tags, etc.)
- **Metadata**: File path, folder category, severity, service name, variables
  list, full JSON
- **Embedding**: 384-dimensional vector (for default model)
- **Variables**: Extracted variable placeholders (e.g.,
  `["TIME", "REASON", "POD"]`) for interpolation

## Contributing

1. Ensure the managed-notifications directory is up to date
2. Run the embedding script after notification changes
3. Test both local and containerized deployments
4. Validate search results for accuracy and relevance
