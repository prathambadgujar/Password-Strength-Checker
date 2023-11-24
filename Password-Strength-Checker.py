import re

def check_password_strength(password):
# Checking for the minimum length
if len(password) < 8:
return "Password is too short. It should be at least 8 characters long."

# Checking for at least one number
if not re.search(r"\d", password):
return "Password should include at least one numeral."

# Checking for at least one uppercase letter
if not re.search(r"[A-Z]", password):
return "Password should include at least one uppercase letter."

# Checking for at least one lowercase letter
if not re.search(r"[a-z]", password):
return "Password should include at least one lowercase letter."

# Checking for at least one special character
if not re.search(r"\W", password):
return "Password should include at least one special character."

return "Password is strong."

def main():
password = input("Enter a password: ")
print(check_password_strength(password))

if __name__ == "__main__":
main()