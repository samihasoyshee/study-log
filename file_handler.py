import csv
import os
from study_session import StudySession
def save_session(session):
    file_exists = os.path.exists("study_sessions.csv")
    with open("study_sessions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date",
                            "Subject",
                            "Hours",
                            "Productivity",
                            "Notes"])

        writer.writerow([
            session.date, 
            session.subject,
            session.hours,
            session.productivity,
            session.notes])
        
def load_sessions():
    sessions = []
    with open("study_sessions.csv","r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            session = StudySession(
                row[0],
                row[1],
                float(row[2]),
                int(row[3]),
                row[4]
            )
            sessions.append(session)
    return sessions
