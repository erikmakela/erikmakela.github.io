import requests
import os
from datetime import datetime

# --- Config ---
USERNAME = "erikmakela"
TOKEN = os.getenv("GH_TOKEN")  # Personal access token from repo secrets
OUTPUT_FILE = "_tabs/github_stars.md"

# Ensure the output directory exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# --- Front matter for Chirpy ---
FRONT_MATTER = """---
# the default layout is 'page'
icon: fas fa-info-circle
order: 5
---
"""

# --- GitHub API headers ---
headers = {
    "Accept": "application/vnd.github.star+json"
}

if TOKEN:
    headers["Authorization"] = f"token {TOKEN}"

# --- Fetch starred repositories ---
url = f"https://api.github.com/users/{USERNAME}/starred"
params = {"per_page": 100}

stars = []

while url:
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    stars.extend(r.json())
    url = r.links.get("next", {}).get("url")

# --- Write Markdown file with front matter ---
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    # Add custom front matter first
    f.write(FRONT_MATTER + "\n")
    
    # Add table header
    f.write("| Repository | Description | ⭐ Stars | ⭐ Starred On |\n")
    f.write("|------------|-------------|--------:|-------------|\n")

    # Add each starred repository as a row
    for item in stars:
        repo = item["repo"]
        name = repo["full_name"]
        link = repo["html_url"]
        desc = (repo["description"] or "").replace("\n", " ")
        star_count = repo["stargazers_count"]
        starred_at = datetime.fromisoformat(item["starred_at"].replace("Z", "+00:00")).date()

        f.write(f"| [{name}]({link}) | {desc} | {star_count} | {starred_at} |\n")

print(f"Saved {len(stars)} starred repositories to {OUTPUT_FILE}")
