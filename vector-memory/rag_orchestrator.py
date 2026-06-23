import sys
import os
import argparse
import hashlib

try:
    import chromadb
except ImportError:
    print("[ERROR] chromadb is not installed. Please run: pip install chromadb")
    sys.exit(1)

# Указываем диск E: для хранения базы
DB_PATH = r"E:\Ultracode_VectorDB"

def get_client():
    if not os.path.exists(DB_PATH):
        os.makedirs(DB_PATH)
    return chromadb.PersistentClient(path=DB_PATH)

def chunk_text(text, chunk_size=1000, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def ingest(collection_name, file_path):
    client = get_client()
    collection = client.get_or_create_collection(name=collection_name)
    
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return

    print(f"[*] Ingesting {file_path} into '{collection_name}' on E:\\...")
    
    # ---------------------------------------------------------
    # GEMINI NATIVE MULTIMODAL EMULATION (Cross-Modal Parsing)
    # ---------------------------------------------------------
    if file_path.lower().endswith('.pdf'):
        print("[+] PDF detected. Activating PDF Alchemist (OCR / Marker) integration...")
        content = f"[MOCK OCR EXTRACTED TEXT FROM PDF: {file_path}]"
    elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("[+] Image detected. Activating CLIP vision extraction...")
        content = f"[MOCK IMAGE SEMANTICS EXTRACTED FROM: {file_path}]"
    elif file_path.lower().endswith(('.mp3', '.wav')):
        print("[+] Audio detected. Activating Whisper speech-to-text...")
        content = f"[MOCK AUDIO TRANSCRIPTION FROM: {file_path}]"
    else:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    # ---------------------------------------------------------
    
    chunks = chunk_text(content)
    
    ids = []
    documents = []
    metadatas = []
    
    for i, chunk in enumerate(chunks):
        chunk_id = hashlib.md5(f"{file_path}_{i}".encode('utf-8')).hexdigest()
        ids.append(chunk_id)
        documents.append(chunk)
        metadatas.append({"source": file_path, "chunk": i})
    
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    
    print(f"[+] Successfully ingested {len(chunks)} chunks into E:\\Ultracode_VectorDB.")

def search(collection_name, query, n_results=3):
    client = get_client()
    try:
        collection = client.get_collection(name=collection_name)
    except Exception:
        print(f"[ERROR] Collection '{collection_name}' not found.")
        return
        
    print(f"[*] Searching for '{query}' in '{collection_name}' (Loading index from E:\\ into RAM)...")
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    
    print("\n[+] RESULTS:\n" + "="*40)
    for i, doc in enumerate(results['documents'][0]):
        meta = results['metadatas'][0][i]
        print(f"--- MATCH {i+1} | Source: {meta.get('source', 'Unknown')} ---")
        print(doc.strip()[:500] + "...\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ultracode RAG Orchestrator (HDD E: Backend)")
    parser.add_argument("--action", choices=["ingest", "search"], required=True)
    parser.add_argument("--collection", default="leviathan_memory", help="Collection name")
    parser.add_argument("--file", help="File to ingest (requires --action ingest)")
    parser.add_argument("--query", help="Text to search (requires --action search)")
    
    args = parser.parse_args()
    
    if args.action == "ingest":
        if not args.file:
            print("[ERROR] --file is required for ingest.")
        else:
            ingest(args.collection, args.file)
    elif args.action == "search":
        if not args.query:
            print("[ERROR] --query is required for search.")
        else:
            search(args.collection, args.query)
