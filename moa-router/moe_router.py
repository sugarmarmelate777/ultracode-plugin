import sys
import json

def analyze_task_and_route(prompt):
    """
    Mock DeepSeek MoE (Mixture of Experts) Router.
    Analyzes the user prompt and selects the specific Expert Sub-Agents to activate.
    This saves tokens by not activating all 30,000 skills for every request.
    """
    prompt = prompt.lower()
    active_experts = []
    
    if "db" in prompt or "database" in prompt or "rag" in prompt or "sql" in prompt:
        active_experts.append("Database Expert (RAG/SQL)")
        
    if "bug" in prompt or "error" in prompt or "fail" in prompt:
        active_experts.append("Debugging & QA Expert")
        
    if "legal" in prompt or "contract" in prompt or "law" in prompt:
        active_experts.append("Legal Expert Swarm")
        
    if "frontend" in prompt or "ui" in prompt or "css" in prompt or "react" in prompt:
        active_experts.append("Frontend UI Architect")
        
    # Fallback to general reasoning if no specific expert is triggered
    if not active_experts:
        active_experts.append("General Reasoning Agent")
        
    routing_plan = {
        "original_prompt": prompt,
        "activated_experts": active_experts,
        "mode": "parallel_execution" if len(active_experts) > 1 else "sequential"
    }
    
    return json.dumps(routing_plan, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python moe_router.py '<task_prompt>'")
        sys.exit(1)
        
    user_prompt = sys.argv[1]
    plan = analyze_task_and_route(user_prompt)
    print(f"[*] DeepSeek MoE Router Activation Plan:\n{plan}")
