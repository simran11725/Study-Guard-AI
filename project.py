#study guard AI 
# Developed by Simranjeet kaur
#AI for social good hackathon project


import time

# List of blocked apps
blocked_apps = ["Instagram", "Facebook", "YouTube"]

study_mode = False



# Focus Mode Functions


def activate_study_mode(duration_minutes):
    global study_mode
    study_mode = True
    print("\n📚 Study Mode Activated")
    print("Social media apps are blocked.")
    print("Only calls are allowed.\n")

    time.sleep(2)
    print(f"Study session started for {duration_minutes} minutes.\n")


def emergency_exit():
    global study_mode
    study_mode = False
    print("\n⚠ Emergency Exit Activated")
    print("Social media temporarily allowed for 2 minutes.\n")
    time.sleep(2)
    print("Focus mode will resume automatically.\n")



# Distraction Awareness


def check_distraction(attempt):
    if attempt.lower() == "yes":
        print("\n AI: You tried to open social media during study time.")
        print("Remember: Your dreams deserve your focus!\n")
    else:
        print("\n AI: Great discipline! Keep going!\n")


# Motivational System


def show_motivation():
    print("\n Motivation: Small focused hours today create big success tomorrow.\n")



# AI Tutor (Basic Demo)


def ai_tutor(question):
    if "photosynthesis" in question.lower():
        return "Photosynthesis is the process by which plants make food using sunlight."
    elif "gravity" in question.lower():
        return "Gravity is the force that pulls objects toward the Earth."
    else:
        return "Let me explain this in a simple way like a YouTube teacher would."


# Main Program

def main():
    print("Welcome to StudyGuard AI")

    activate_study_mode(60)

    check_distraction("yes")

    show_motivation()

    doubt = input("Ask your study doubt: ")
    answer = ai_tutor(doubt)

    print("\n AI Tutor Answer:")
    print(answer)

    emergency_exit()


if __name__ == "__main__":
    main()