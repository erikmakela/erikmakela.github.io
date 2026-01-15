import requests
import os
from datetime import datetime

USERNAME = "erikmakela"
TOKEN = os.getenv("GH_TOKEN")  # Optional: "ghp_xxxxxxxxxxxxxxxxxxxx"
OUTPUT_FILE = "_tabs/github_stars.md"

headers = {
    # Required to get `starred_at`
    "Accept": "application/vnd.github.star+json"
}

if TOKEN:
    headers["Authorization"] = f"token {TOKEN}"

url = f"https://api.github.com/users/{USERNAME}/starred"
params = {"per_page": 100}

stars = []

while url:
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    stars.extend(r.json())
    url = r.links.get("next", {}).get("url")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("| Repository | Description | ⭐ Stars | ⭐ Starred On |\n")
    f.write("|------------|-------------|--------:|-------------|\n")

    for item in stars:
        repo = item["repo"]
        name = repo["full_name"]
        link = repo["html_url"]
        desc = (repo["description"] or "").replace("\n", " ")
        star_count = repo["stargazers_count"]
        starred_at = datetime.fromisoformat(
            item["starred_at"].replace("Z", "+00:00")
        ).date()

        f.write(
            f"| [{name}]({link}) | {desc} | {star_count} | {starred_at} |\n"
        )

print(f"Saved {len(stars)} starred repositories to {OUTPUT_FILE}")

