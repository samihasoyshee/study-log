from file_handler import save_session
from datetime import datetime
def add_study_session():
    print("\n Add Study Session\n")
    subject = input("Subject: ")
    hours = float(input("Hours Studied: "))
    productivity = int(input("Productivity(1-10): "))
    notes = input("Notes: ")
    date = datetime.now().strftime("%d-%m-%Y")

    print("\n===Study Session===\n")
    print(f"Date: {date}")
    print(f"Subject: {subject}")
    print(f"Hours: {hours}")
    print(f"Productivity: {productivity}")
    print(f"Notes: {notes}")

    save_session(date, subject, hours, productivity, notes)
    print("\nStudy Session saved successfully!")    