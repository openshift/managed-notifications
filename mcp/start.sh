#!/bin/sh
echo "Building embeddings database (this may take 2-5 minutes)..."
uv run --no-sync scripts/build_embeddings.py
echo "Embeddings built, starting MCP server..."
exec uv run --no-sync main.py