import csv
import os
def save_session(date, subject, hours, productivity, notes):
    file_exists = os.path.exists("study_sessions.csv")
    with open("study_sessions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Subject", "Hours", "Productivity", "Notes"])

        writer.writerow([date, subject, hours, productivity, notes])