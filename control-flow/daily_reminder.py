# File: control-flow/daily_reminder.py

def main():
    # Get user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match case for priority
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            print("Invalid priority level entered. Please choose high, medium, or low.")
            return

    # Add urgency if time-bound
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    elif time_bound == "no":
        message += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity. Please enter yes or no.")
        return

    # Output the final message
    print("\n" + message)

if __name__ == "__main__":
    main()
