🚀 Python Entry-Level Job Hunter
A lightweight, automated Python script designed to scrape, score, and notify you about the best entry-level software engineering roles using SerpApi and Discord Webhooks.

Stop manually refreshing job boards. This script does the heavy lifting by identifying high-match roles based on title, description, and seniority level, then pings your Discord server with the results.

✨ Key Features
Smart Scoring System: Ranks jobs based on keywords and preferred skills (e.g., Python, React, AWS) to ensure you see the most relevant roles first.

Automatic Filtering: Hard-coded exclusion of "Senior," "Lead," and "Manager" roles to keep your feed strictly entry-level/junior.

Deduplication: Maintains a seen_jobs.json file to ensure you never get notified about the same job twice.

Discord Integration: Delivers formatted job alerts—including title, company, location, and application link—directly to your Discord channel.

Customizable Queries: Easily modify search terms like "backend engineer" or "remote software developer" to fit your niche.

🛠️ Tech Stack
Language: Python 3.x

APIs: Google Jobs via SerpApi

Notifications: Discord Webhooks

Libraries: requests, hashlib, json



⚙️ Setup
Clone the repo.

Environment Variables: Set your SERPAPI_KEY and DISCORD_WEBHOOK in your environment.

Install Requirements: pip install requests.

Run: python main.py.

📝 Configuration
You can fine-tune the search behavior directly in the CONFIG section of the script:

DAILY_LIMIT: Max number of jobs to post per run.

MIN_SCORE: Minimum "match score" required for a job to be sent to Discord.

SEARCH_QUERIES: Tailor the list of terms the script searches for.
