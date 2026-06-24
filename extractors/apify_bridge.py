import os
import sys
from apify_client import ApifyClient

def extract_with_apify(actor_id, run_input):
    api_token = os.environ.get("APIFY_API_TOKEN")
    if not api_token:
        print("Error: APIFY_API_TOKEN environment variable is not set.")
        sys.exit(1)

    print(f"Starting Apify Actor: {actor_id}")
    client = ApifyClient(api_token)
    
    try:
        run = client.actor(actor_id).call(run_input=run_input)
        print("--- EXTRACTION SUCCESSFUL ---")
        dataset = client.dataset(run["defaultDatasetId"]).list_items().items
        import json
        print(json.dumps(dataset, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Failed to run Apify actor: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python apify_bridge.py <ACTOR_ID> <INPUT_JSON>")
        print("Example: python apify_bridge.py apify/instagram-scraper '{\"username\": [\"nike\"]}'")
        sys.exit(1)
    
    import json
    actor = sys.argv[1]
    input_data = json.loads(sys.argv[2])
    extract_with_apify(actor, input_data)
