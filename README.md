# Job Application Tracker

A lightweight Python command-line tool that reads a CSV of job applications and generates a clean summary report — built to solve a real problem during an active job search.

---

## The Problem

I built this to help me stay on track during job searching. Tracking everything in a spreadsheet worked fine for storage, but I had no quick way to answer:

- How many applications have I sent in the last week?
- Which pending roles have gone cold and need a follow-up?
- What's my current pipeline breakdown by status?

Scrolling through rows manually every morning was slow and error-prone. I wanted a script I could run in seconds to get a structured snapshot.

---

## What It Does

Run `python job_tracker.py` from the same folder as your `applications.csv` and it outputs:

- **Total applications** and recent activity (last 7 and 30 days)
- **Status breakdown** with a visual bar chart (Pending / Interview Scheduled / Offer Received / Rejected)
- **Follow-up alerts** — any role that has been Pending for 14+ days is flagged automatically
- **Recent activity log** — all applications from the last 7 days with date, company, role, and status

---

## How to Use

**1. Clone or download this repo**

**2. Edit `applications.csv` with your own data**

The CSV uses five columns:

| Column | Description | Example |
|---|---|---|
| `company` | Company name | Anduin |
| `role` | Job title | Task Force |
| `date_applied` | Date in MM/DD/YYYY format | 10/11/2026 |
| `status` | Current status | Pending |
| `notes` | Any notes (optional) | Vietnam role |

Valid status values: `Pending`, `Interview Scheduled`, `Offer Received`, `Rejected`

**3. Run the script**

```bash
python job_tracker.py
```
## Here’s how I run it:

1. Unzip the folder
2. Open File Explorer → navigate into the job_tracker folder
3. Click the address bar at the top → type `cmd` → press Enter
    -> This opens a terminal already pointed at that folder
4. Type: `python job_tracker.py` → press Enter
5. The report prints right there in the terminal window


No external libraries required — uses only Python standard library (`csv`, `datetime`, `collections`, `os`).

---

## Sample Output

```
==================================================
  JOB APPLICATION TRACKER — SUMMARY REPORT
  Generated: October 11, 2026
==================================================

  Total Applications: 9
  Applied in last  7 days: 5
  Applied in last 30 days: 9

  Status Breakdown:
--------------------------------------------------
  Interview Scheduled    1  █
  Offer Received         1  █
  Pending                6  ██████
  Rejected               1  █
--------------------------------------------------

  ⚠  Follow-Up Needed (14+ days, still Pending):
--------------------------------------------------
  YouNet Media              Product Support Executive      applied 16 days ago
--------------------------------------------------
```

---

## Why I Built It This Way

- **No dependencies** — runs anywhere Python is installed, no pip install needed
- **CSV input** — easy to edit in Excel or Google Sheets, no database setup
- **Configurable follow-up window** — change `FOLLOWUP_DAYS` at the top of the script to adjust the alert threshold
- **Extensible** — the core logic is modular; adding email alerts, charts, or a web UI would be straightforward next steps

---

## Tech

- Python 3.x
- Standard library only: `csv`, `datetime`, `collections`, `os`

---

*Built by Hoang Tue Anh — October 2026*
