"""
Job Application Tracker
-----------------------
Reads a CSV of job applications and generates a summary report:
- Total applications and breakdown by status
- Recent activity (last 7 and 30 days)
- Roles that may need a follow-up (applied 14+ days ago, still Pending)
"""

import csv
import os
from datetime import datetime, timedelta
from collections import Counter


CSV_FILE = "applications.csv"
DATE_FORMAT = "%m/%d/%Y"
FOLLOWUP_DAYS = 14


def load_applications(filepath):
    if not os.path.exists(filepath):
        print(f"Error: '{filepath}' not found. Make sure it's in the same folder as this script.")
        return []

    applications = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):  # start=2 because row 1 is header
            # Clean up whitespace
            row = {k: v.strip() for k, v in row.items()}

            # Parse date
            try:
                row["date_applied"] = datetime.strptime(row["date_applied"], DATE_FORMAT)
            except ValueError:
                print(f"  Warning: Row {i} has an invalid date '{row['date_applied']}' — skipping.")
                continue

            applications.append(row)

    return applications


def print_separator(char="-", width=50):
    print(char * width)


def generate_report(applications):
    if not applications:
        print("No applications found.")
        return

    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    last_7  = today - timedelta(days=7)
    last_30 = today - timedelta(days=30)
    followup_cutoff = today - timedelta(days=FOLLOWUP_DAYS)

    total = len(applications)
    status_counts = Counter(app["status"] for app in applications)
    recent_7  = [a for a in applications if a["date_applied"] >= last_7]
    recent_30 = [a for a in applications if a["date_applied"] >= last_30]
    needs_followup = [
        a for a in applications
        if a["status"].lower() == "pending" and a["date_applied"] <= followup_cutoff
    ]

    # ── Header ──────────────────────────────────────────
    print()
    print_separator("=")
    print("  JOB APPLICATION TRACKER — SUMMARY REPORT")
    print(f"  Generated: {today.strftime('%B %d, %Y')}")
    print_separator("=")

    # ── Overview ────────────────────────────────────────
    print(f"\n  Total Applications: {total}")
    print(f"  Applied in last  7 days: {len(recent_7)}")
    print(f"  Applied in last 30 days: {len(recent_30)}")

    # ── Status Breakdown ────────────────────────────────
    print("\n  Status Breakdown:")
    print_separator()
    for status, count in sorted(status_counts.items()):
        bar = "█" * count
        print(f"  {status:<20} {count:>3}  {bar}")
    print_separator()

    # ── Follow-Up Needed ────────────────────────────────
    if needs_followup:
        print(f"\n  ⚠  Follow-Up Needed ({FOLLOWUP_DAYS}+ days, still Pending):")
        print_separator()
        for app in sorted(needs_followup, key=lambda x: x["date_applied"]):
            days_ago = (today - app["date_applied"]).days
            print(f"  {app['company']:<25} {app['role']:<30} applied {days_ago} days ago")
        print_separator()
    else:
        print(f"\n  ✓  No pending applications older than {FOLLOWUP_DAYS} days.")

    # ── Recent Activity ──────────────────────────────────
    if recent_7:
        print(f"\n  Applied in the Last 7 Days:")
        print_separator()
        for app in sorted(recent_7, key=lambda x: x["date_applied"], reverse=True):
            print(f"  {app['date_applied'].strftime('%b %d'):<8} {app['company']:<25} {app['role']:<30} [{app['status']}]")
        print_separator()

    print()


def main():
    print(f"Loading applications from '{CSV_FILE}'...")
    applications = load_applications(CSV_FILE)
    print(f"Loaded {len(applications)} application(s).")
    generate_report(applications)


if __name__ == "__main__":
    main()
