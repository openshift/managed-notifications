"""Build embeddings for managed service notification logs."""

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Union, Mapping

import chromadb
from sentence_transformers import SentenceTransformer


def load_embedding_model() -> SentenceTransformer:
    """Load the sentence transformer model for creating embeddings."""
    model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    return SentenceTransformer(model_name)


def extract_variables(text: str) -> List[str]:
    """Extract variable placeholders from text (e.g., ${VARIABLE_NAME})."""
    if not text:
        return []
    
    # Find all ${VARIABLE_NAME} patterns
    pattern = r'\$\{([^}]+)\}'
    variables = re.findall(pattern, text)
    return sorted(list(set(variables)))  # Remove duplicates and sort


def extract_searchable_text(notification_data: Dict[str, Any]) -> str:
    """Extract searchable text from notification JSON data."""
    searchable_fields = ["summary", "description", "log_type", "service_name"]
    text_parts = []
    
    for field in searchable_fields:
        if field in notification_data and notification_data[field]:
            text_parts.append(str(notification_data[field]))
    
    if "_tags" in notification_data and notification_data["_tags"]:
        text_parts.extend(notification_data["_tags"])
    
    return " ".join(text_parts)


def get_folder_metadata(file_path: Path, base_path: Path) -> str:
    """Extract folder metadata from file path."""
    relative_path = file_path.relative_to(base_path)
    if len(relative_path.parts) > 1:
        return relative_path.parts[0]
    return "root"


def process_notification_files(notifications_dir: Path) -> tuple[list[str], list[Mapping[str, Union[str, int, float, bool, None]]], list[str]]:
    """Process all JSON notification files and extract data for embeddings."""
    documents = []
    metadatas: list[Mapping[str, Union[str, int, float, bool, None]]] = []
    ids = []
    
    json_files = list(notifications_dir.rglob("*.json"))
    print(f"Found {len(json_files)} JSON files to process")
    
    for idx, json_file in enumerate(json_files):
        try:
            with json_file.open("r", encoding="utf-8") as f:
                notification_data = json.load(f)
            
            searchable_text = extract_searchable_text(notification_data)
            if not searchable_text.strip():
                continue
            
            folder_tag = get_folder_metadata(json_file, notifications_dir)
            
            # Extract variables from all text fields
            all_variables = set()
            for field in ["summary", "description"]:
                if field in notification_data and notification_data[field]:
                    all_variables.update(extract_variables(str(notification_data[field])))
            
            documents.append(searchable_text)
            metadatas.append({
                "file_path": str(json_file.relative_to(notifications_dir)),
                "folder": folder_tag,
                "severity": notification_data.get("severity", "Unknown"),
                "service_name": notification_data.get("service_name", "Unknown"),
                "log_type": notification_data.get("log_type", "Unknown"),
                "internal_only": notification_data.get("internal_only", False),
                "variables": json.dumps(sorted(list(all_variables))),  # Store as JSON string
                "full_json": json.dumps(notification_data)
            })
            ids.append(f"notification_{idx}")
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error processing {json_file}: {e}")
            continue
    
    print(f"Successfully processed {len(documents)} notifications")
    return documents, metadatas, ids


def test_search(model: SentenceTransformer, collection) -> None:
    """Test the database with a sample search query."""
    test_query = "missing or insufficient permissions"
    print(f"Searching for: '{test_query}'")
    
    # Create embedding for test query
    query_embedding = model.encode([test_query])
    
    # Search in ChromaDB
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=3
    )
    
    if results['documents'] and len(results['documents'][0]) > 0:
        print(f"✓ Found {len(results['documents'][0])} matching results:")
        for i, doc in enumerate(results['documents'][0]):
            distance = results['distances'][0][i] if 'distances' in results else 0.0
            similarity = 1 - distance
            metadata = results['metadatas'][0][i]
            print(f"  {i+1}. [{metadata.get('folder', 'unknown')}/{metadata.get('file_path', 'unknown')}] "
                  f"(similarity: {similarity:.3f})")
            print(f"     {doc[:100]}...")
    else:
        print("✗ No results found - this may indicate an issue with the database")
    
    print()


def build_embeddings_database(notifications_dir: Path, db_path: Path) -> None:
    """Build the ChromaDB embeddings database."""
    print("Loading embedding model...")
    model = load_embedding_model()
    
    print("Processing notification files...")
    documents, metadatas, ids = process_notification_files(notifications_dir)
    
    if not documents:
        print("No documents to process. Exiting.")
        return
    
    print("Creating embeddings...")
    embeddings = model.encode(documents, show_progress_bar=True)
    
    print("Setting up ChromaDB...")
    if db_path.exists():
        import shutil
        shutil.rmtree(db_path)
    
    db_path.mkdir(parents=True, exist_ok=True)
    
    client = chromadb.PersistentClient(path=str(db_path))
    
    collection_name = "managed_notifications"
    try:
        client.delete_collection(collection_name)
    except (ValueError, Exception):
        # Collection doesn't exist, which is fine
        pass
    
    collection = client.create_collection(
        name=collection_name,
        metadata={"description": "Managed service notification logs"}
    )
    
    print("Adding embeddings to ChromaDB...")
    collection.add(
        embeddings=embeddings.tolist(),
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    
    print(f"Successfully added {len(documents)} documents to ChromaDB")
    print(f"Database saved to: {db_path}")
    
    # Test the database with a sample search
    print("\nTesting database with sample search...")
    test_search(model, collection)


def main() -> None:
    """Main function to build embeddings database."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    notifications_dir = project_root / "managed-notifications"
    db_path = project_root / "chroma_db"
    
    if not notifications_dir.exists():
        print(f"Error: Managed notifications directory not found at {notifications_dir}")
        return
    
    print(f"Building embeddings for notifications in: {notifications_dir}")
    print(f"Database will be saved to: {db_path}")
    
    build_embeddings_database(notifications_dir, db_path)


if __name__ == "__main__":
    main()