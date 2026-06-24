import sys
import asyncio
from crawl4ai import AsyncWebCrawler

async def extract_webpage(url):
    print(f"Starting extraction for URL: {url}")
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
            bypass_cache=True
        )
        if result.success:
            print("--- EXTRACTION SUCCESSFUL ---")
            print(result.markdown)
        else:
            print(f"Failed to extract URL: {result.error_message}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python web_extractor.py <URL>")
        sys.exit(1)
    
    target_url = sys.argv[1]
    asyncio.run(extract_webpage(target_url))
