from session_manager import add_study_session
def main():
    print("." * 20)
    print("     StudyLog")
    print("." * 20)
    print("1. Add Study Session")
    print("2. Exit")

main()
choice = input("Enter your option: ")
if choice == "1":
    add_study_session()
elif choice == "2":
    print("Goodbye!")
else:
    print("Invalid choice! Please try again.")