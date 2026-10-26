#!/usr/bin/env python3
"""
Automation step: draft a weekly security-habit reminder from the checklist.

Run:   python3 weekly_reminder.py            -> prints this week's reminder
       python3 weekly_reminder.py --all      -> writes weekly_reminders.md (12 weeks)

How to automate for free (no code needed after this):
  * Paste the weekly text into a repeating Google Calendar event / phone reminder, or
  * Make.com / Notion: a weekly scheduled scenario that posts the text to a hostel
    WhatsApp/Telegram group or emails it to you.
Nothing here touches real accounts or passwords.
"""
import argparse
import datetime

# Each tip comes straight from the Habit Checklist (01_habit_checklist.md).
TIPS = [
    ("Email first", "Give your main email a unique 5-6 word passphrase and turn on MFA. Email resets every other account."),
    ("Password manager day", "Install a password manager and move 3 accounts into it. Save your master passphrase to memory - not a chat."),
    ("Recovery codes", "Print or write your recovery codes and keep them in a locked place, not in WhatsApp or Notes."),
    ("OTP is private", "Rule: nobody ever needs your OTP - not a bank, a hostel office, a scholarship desk, or a friend. Hang up and call back on the official number."),
    ("Reuse check", "Open your manager's reuse/weak report. Fix the 3 most important reused passwords (email, banking, college portal)."),
    ("Prompt discipline", "Got a login approval you didn't start? Tap DENY, then change that account's password."),
    ("Shared devices", "Using a lab, cyber-cafe or friend's laptop? Use a private window, never 'remember me', and sign out everywhere after."),
    ("Upgrade your MFA", "Move one key account from SMS codes to an authenticator app (or passkey / security key if supported)."),
    ("Account clean-up", "Delete 3 old accounts you no longer use. Fewer accounts = fewer breaches to worry about."),
    ("Phone safety", "Set a screen-lock PIN and install updates. Your phone is now your second factor."),
    ("Breach check", "Check your own email on the official Have I Been Pwned site. If it shows a breach, change that password and anywhere you reused it."),
    ("Teach one friend", "Show one hostel-mate how to turn on MFA on their email. Habits stick when shared."),
]


def week_message(week_index: int) -> str:
    title, body = TIPS[week_index % len(TIPS)]
    return f"Week {week_index + 1} - {title}\n{body}\nTakes 10 minutes. Do it today."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    if args.all:
        with open("weekly_reminders.md", "w", encoding="utf-8") as f:
            f.write("# 12-week security-habit reminders (draft)\n\n")
            for i in range(len(TIPS)):
                f.write(f"## {week_message(i).splitlines()[0]}\n\n" + "\n".join(week_message(i).splitlines()[1:]) + "\n\n")
        print("Wrote weekly_reminders.md")
    else:
        week = datetime.date.today().isocalendar()[1]
        print(week_message(week % len(TIPS)))


if __name__ == "__main__":
    main()
