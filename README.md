# 🚀 JobFinder-Py: Automated Entry-Level Scout

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

**JobFinder-Py** is a lightweight automation tool designed to help junior developers break through the noise of the job market. It automatically scrapes, scores, and filters Software Engineering roles, delivering high-quality leads directly to your **Discord** server.

---

## 📖 Table of Contents
* [Key Features](#-key-features)
* [How It Works](#-how-it-works)
* [Installation](#-installation)
* [Configuration](#-configuration)
* [Usage](#-usage)
* [License](#-license)

---

## ✨ Key Features

*   **🎯 Smart Seniority Filtering**: Automatically ignores roles containing keywords like **Senior**, **Staff**, **Principal**, or **Manager** to keep results relevant for entry-level talent.
*   **📊 Weighted Scoring System**: Ranks jobs based on your specific stack (e.g., **Python**, **React**, **AWS**) and prioritizes them in your feed.
*   **🚫 Duplicate Prevention**: Uses a local `seen_jobs.json` database to ensure you **never receive the same job notification twice**.
*   **🤖 Discord Integration**: Sends beautifully formatted notifications including **Job Title**, **Company**, **Location**, and a **Direct Apply Link**.
*   **🔍 Multi-Query Support**: Search for multiple titles (e.g., "Frontend Developer" and "Python Intern") in a single run.

---

## ⚙️ How It Works

The script follows a simple 4-step pipeline:

1.  **Fetch**: Queries the **Google Jobs API** via SerpApi based on your custom query list.
2.  **Filter**: Scrubs titles for "blacklist" words to ensure the role isn't mid-to-senior level.
3.  **Score**: Analyzes the description for **Preferred Skills**; higher scores indicate a better match for your resume.
4.  **Notify**: If a job is new and passes the **Minimum Score** threshold, it pings your Discord Webhook.

---

## 🛠 Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/job-finder-py.git](https://github.com/yourusername/job-finder-py.git)
cd job-finder-py
```
### 2. Install Dependencies
```bash
pip install requests
```
### 3. Set Up Environment Variables
The script requires two keys to function. Export them to your environment:
```bash
export SERPAPI_KEY='your_serp_api_key_here'
export DISCORD_WEBHOOK='your_discord_webhook_url_here'
```
### 4.🔧 Configuration
Fine-tune the search logic within the CONFIG section of main.py:
| Variable | Description | Default |
|----------|-------------|---------|
| `SEARCH_QUERIES` | List of titles to search for. | `["junior software engineer", ...]` |
| `PREFERRED_SKILLS` | Tech that increases the "Match Score." | `["python", "react", "sql", ...]` |
| `MIN_SCORE` | Points required to trigger a notification. | `5` |
| `DAILY_LIMIT` | Maximum jobs to post per run. | `15` |
| `EXCLUDE` | Keywords that disqualify a job instantly. | `["senior", "lead", "staff"]` |   


🚀 Usage
To run the script manually:
```bash
python main.py
```
[!TIP]
Automation: Set this up as a GitHub Action or a Cron Job to run every morning at 9:00 AM so you are always the first to apply!

📄 License
Distributed under the MIT License. See LICENSE for more information.
Disclaimer: This tool uses SerpApi which may incur costs depending on your usage tier. Use responsibly.
