from file_handler import save_session, load_sessions
from datetime import datetime
from study_session import StudySession
def add_study_session():
    print("\nStudy Session\n")
    subject = input("Subject: ")
    hours = float(input("Hours Studied: "))
    productivity = int(input("Productivity(1-10): "))
    notes = input("Notes: ")
    date = datetime.now().strftime("%d-%m-%Y")

    session = StudySession(
        date, subject, hours, productivity, notes)
    
    save_session(session)
    session.display()

def view_all_sessions():
    sessions = load_sessions()
    for session in sessions:
        session.display()
    
print("\nStudy Session saved successfully!")  

def search_by_subject():
    subject = input("Enter your subject: ")

    sessions = load_sessions()

    found= False
    for session in sessions:
        if subject == session.subject:
            session.display()
            found = True
    if not found:
        print("No study session found!")
