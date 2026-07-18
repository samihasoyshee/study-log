import csv
import os
def save_session(session):
    file_exists = os.path.exists("study_sessions.csv")
    with open("study_sessions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Subject", "Hours", "Productivity", "Notes"])

        writer.writerow([
            session.date, 
            session.subject,
              session.hours,
                session.productivity,
                  session.notes])