import re
import getpass

def check_password_strength(password):
    # List to hold failure messages
    failure_messages = []

    # Checking for the minimum length
    if len(password) < 8:
        failure_messages.append("It should be at least 8 characters long.")

    # Checking for at least one number
    if not re.search(r"\d", password):
        failure_messages.append("It should include at least one numeral.")

    # Checking for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        failure_messages.append("It should include at least one uppercase letter.")

    # Checking for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        failure_messages.append("It should include at least one lowercase letter.")

    # Checking for at least one special character
    if not re.search(r"\W", password):
        failure_messages.append("It should include at least one special character.")

    # Classifying password strength and creating feedback message
    if not failure_messages:
        strength_message = "Your password is strong."
    elif len(failure_messages) >= 3:
        strength_message = "Your password is weak."
    elif len(failure_messages) == 2:
        strength_message = "Your password is medium."
    else:
        strength_message = "Your password is strong, but could be stronger."

    # Formatting failure messages with spaces between each message
    feedback_message = "\n\n".join(failure_messages)

    return strength_message, feedback_message

def main():
    while True:
        password = getpass.getpass("Enter a password: ")
        print("\nChecking password strength...\n")  # Adding line breaks

        strength_message, feedback_message = check_password_strength(password)

        print(strength_message.upper() + '\n')
        if feedback_message:
            # Replace password characters with "*"
            hidden_password = '*' * len(password)
            print("To increase the strength of your password:\n")
            print(feedback_message.replace(password, hidden_password) + '\n')
        else:
            break  # If the password is strong, exit the loop

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
