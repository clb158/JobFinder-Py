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
