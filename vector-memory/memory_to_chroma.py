import chromadb
import os
import glob
from uuid import uuid4

CHROMA_PATH = r"E:\Ultracode_VectorDB"
MEMORY_BANK_DIR = "memory-bank"

def index_memory_bank():
    print(f"Connecting to ChromaDB at {CHROMA_PATH}...")
    try:
        client = chromadb.PersistentClient(path=CHROMA_PATH)
        collection = client.get_or_create_collection(name="cline_memory_bank")
        
        if not os.path.exists(MEMORY_BANK_DIR):
            print("No memory-bank directory found. Nothing to index.")
            return

        files = glob.glob(os.path.join(MEMORY_BANK_DIR, "*.md"))
        if not files:
            print("Memory bank is empty.")
            return
            
        print(f"Found {len(files)} files to index.")
        
        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            doc_id = f"mem_{os.path.basename(file)}_{uuid4().hex[:6]}"
            
            # Simple chunking by paragraphs (simplified for demonstration)
            chunks = [c.strip() for c in content.split('\n\n') if c.strip()]
            
            if chunks:
                ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
                metadatas = [{"source": file, "type": "memory-bank"} for _ in chunks]
                
                collection.upsert(
                    documents=chunks,
                    metadatas=metadatas,
                    ids=ids
                )
                print(f"Indexed {file} ({len(chunks)} chunks).")
                
        print("Vector indexing complete! Memory Bank is now available via RAG.")
    except Exception as e:
        print(f"Failed to connect to ChromaDB or index data: {e}")

if __name__ == "__main__":
    index_memory_bank()
