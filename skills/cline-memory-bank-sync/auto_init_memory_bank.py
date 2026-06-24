import os
import glob
import json
import requests

DEEPSEEK_URL = "http://localhost:8082/v1/chat/completions"
MEMORY_BANK_DIR = "memory-bank"

def scan_project():
    """Scans the project to extract basic structure and README content."""
    files = glob.glob("*.*")
    folders = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
    
    readme_content = ""
    for file in files:
        if file.lower() == "readme.md":
            with open(file, 'r', encoding='utf-8') as f:
                readme_content = f.read()
                break
                
    return files, folders, readme_content

def ask_llm(prompt):
    """Sends a request to local DeepSeek Engine."""
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "deepseek-coder",
        "messages": [
            {"role": "system", "content": "You are a senior software architect initializing a Cline Memory Bank."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }
    
    try:
        response = requests.post(DEEPSEEK_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Failed to reach DeepSeek Engine at {DEEPSEEK_URL}: {e}")
        return None

def main():
    if not os.path.exists(MEMORY_BANK_DIR):
        os.makedirs(MEMORY_BANK_DIR)
        print(f"Created {MEMORY_BANK_DIR}/ directory.")
        
    print("Scanning project structure...")
    files, folders, readme = scan_project()
    
    project_context = f"Project files: {files}\nFolders: {folders}\nREADME:\n{readme[:2000] if readme else 'No README found.'}"
    
    templates = {
        "projectbrief.md": "Generate a highly concise 'Project Brief' (100-200 words) summarizing the core requirements and goals of this project, based on the following context:\n",
        "productContext.md": "Generate a 'Product Context' explaining why this project exists and what problems it solves, based on the following context:\n",
        "techContext.md": "List the technologies, dependencies, and development setup based on the following context:\n"
    }
    
    for filename, prompt_template in templates.items():
        filepath = os.path.join(MEMORY_BANK_DIR, filename)
        if os.path.exists(filepath):
            print(f"{filename} already exists, skipping.")
            continue
            
        print(f"Generating {filename} via DeepSeek Engine...")
        content = ask_llm(prompt_template + project_context)
        
        if content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Saved {filename}.")
        else:
            print(f"Skipping {filename} due to LLM error. Will create an empty template.")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {filename}\n\n(Auto-generation failed)")
                
    # Create empty ones for dynamic state
    for dynamic in ["activeContext.md", "systemPatterns.md", "progress.md"]:
        filepath = os.path.join(MEMORY_BANK_DIR, dynamic)
        if not os.path.exists(filepath):
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {dynamic}\n\nThis file should be updated actively during development.")
            print(f"Created empty {dynamic}.")
            
    print("Memory Bank AI Auto-Fill complete!")

if __name__ == "__main__":
    main()
