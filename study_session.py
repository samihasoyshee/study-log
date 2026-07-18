class StudySession:
    def __init__(self, date, subject, hours, productivity, notes):
        self.date=date
        self.subject=subject
        self.hours = hours
        self.productivity = productivity
        self.notes = notes
    def display(self):
        print("\n===Study Session===\n")
        print(f"Date: {self.date}")
        print(f"Subject: {self.subject}")
        print(f"Hours: {self.hours}")
        print(f"Productivity: {self.productivity}")
        print(f"Notes: {self.notes}")



