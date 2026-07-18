from file_handler import save_session
from datetime import datetime
from study_session import StudySession
def add_study_session():
    print("\n Add Study Session\n")
    subject = input("Subject: ")
    hours = float(input("Hours Studied: "))
    productivity = int(input("Productivity(1-10): "))
    notes = input("Notes: ")
    date = datetime.now().strftime("%d-%m-%Y")

    session = StudySession(
        date, subject, hours, productivity, notes)
    
    save_session(session)

    
    session.display()


        
    print("\nStudy Session saved successfully!")    