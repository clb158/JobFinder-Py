import requests
import hashlib
import json
import os
import time

# ================= CONFIG =================
SERPAPI_KEY = os.environ["SERPAPI_KEY"]
DISCORD_WEBHOOK = os.environ["DISCORD_WEBHOOK"]

DAILY_LIMIT = 15
MIN_SCORE = 5

SEARCH_QUERIES = [
    "software engineer entry level",
    "junior software engineer",
    "software developer entry level",
    "backend engineer entry level",
    "full stack developer entry level",
    "remote software engineer entry level",
]

LOCATION = "United States"
SEEN_FILE = "seen_jobs.json"

# ==========================================

INCLUDE_KEYWORDS = [
    "software engineer", "software developer", "backend engineer",
    "backend developer", "full stack", "web developer",
    "frontend developer", "application developer", "programmer", "engineer"
]

EXCLUDE = ["senior", "lead", "principal", "manager", "director", "staff"]

PREFERRED_SKILLS = [
    "python", "javascript", "typescript", "java", "c#", "c++",
    "react", "node", "express", "django", "flask", "spring",
    "sql", "postgres", "mysql", "mongodb",
    "api", "rest", "graphql", "aws", "azure", "docker",
    "git", "linux", "debugging", "testing"
]

# ================= STORAGE =================

def load_seen_jobs():
    if not os.path.exists(SEEN_FILE):
        return set()
    with open(SEEN_FILE) as f:
        return set(json.load(f))

def save_seen_jobs(data):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(data), f)

# ================= HELPERS =================

def get_job_id(job):
    return hashlib.md5(
        (job.get("title", "") + job.get("company_name", "") + job.get("location", "")).encode()
    ).hexdigest()

def get_link(job):
    if job.get("apply_options"):
        return job["apply_options"][0].get("link", "")
    return job.get("link", "")

def score_job(job):
    title = job.get("title", "").lower()
    desc = job.get("description", "").lower()
    score = 0
    for k in INCLUDE_KEYWORDS:
        if k in title:
            score += 2
    if any(x in title for x in ["junior", "entry", "associate", "intern"]):
        score += 3
    score += sum(1 for s in PREFERRED_SKILLS if s in desc)
    return score

def is_valid(job):
    title = job.get("title", "").lower()
    return not any(x in title for x in EXCLUDE)

# ================= FETCH =================

def fetch_jobs():
    url = "https://serpapi.com/search.json"
    all_jobs = []

    for query in SEARCH_QUERIES:
        params = {
            "engine": "google_jobs",
            "q": query,
            "location": LOCATION,
            "api_key": SERPAPI_KEY,
            "num": 10
        }

        data = requests.get(url, params=params).json()

        if "error" in data:
            print(f"API ERROR for '{query}':", data["error"])
            continue

        all_jobs.extend(data.get("jobs_results", []))
        time.sleep(0.5)

    return all_jobs

# ================= DISCORD WEBHOOK =================

def post_to_discord(jobs):
    if not jobs:
        payload = {"content": "📭 No new matching jobs found today."}
        requests.post(DISCORD_WEBHOOK, json=payload)
        return

    # Header message
    requests.post(DISCORD_WEBHOOK, json={
        "content": f"🔥 **TODAY'S TOP JOB MATCHES** — {len(jobs)} new jobs found"
    })
    time.sleep(0.5)

    for job, score in jobs:
        link = get_link(job)
        content = (
            f"**{job.get('title')}** · Score: {score}\n"
            f"🏢 {job.get('company_name')}\n"
            f"📍 {job.get('location')}\n"
            f"🔗 {link}"
        )
        requests.post(DISCORD_WEBHOOK, json={"content": content})
        time.sleep(0.3)  # avoid Discord rate limits

# ================= MAIN =================

def main():
    print("Fetching jobs...")
    jobs = fetch_jobs()
    print(f"Fetched {len(jobs)} raw results")

    seen = load_seen_jobs()

    scored = [(j, score_job(j)) for j in jobs if is_valid(j)]
    scored.sort(key=lambda x: x[1], reverse=True)

    new_jobs = []
    for job, score in scored:
        jid = get_job_id(job)
        link = get_link(job)
        if not link or jid in seen:
            continue
        if score >= MIN_SCORE:
            new_jobs.append((job, score))
        if len(new_jobs) >= DAILY_LIMIT:
            break

    print(f"Found {len(new_jobs)} new high-match jobs")

    # Mark as seen
    for job, _ in new_jobs:
        seen.add(get_job_id(job))
    save_seen_jobs(seen)

    post_to_discord(new_jobs)
    print("Done.")

if __name__ == "__main__":
    main()
