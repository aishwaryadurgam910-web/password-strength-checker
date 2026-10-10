import re

password = input ("Enter your password: ")

score = 0
common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome"
]

if len(password) >= 8:
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[0-9]", password):
    score += 1

if re.search(r"[^a-zA-Z0-9]", password):
    score += 1

if score <= 2:
    strength = "WEAK"
elif score <= 4:
    strength = "MEDIUM"
else:
    strength = "STRONG"

print("Password Strength:", strength)
print("Security Score:", score, "/5")

if score < 5:
    print("\nSuggestions:")

    if len(password) < 8:
        print("- Use at least 8 characters.")

    if not re.search(r"[a-z]", password):
        print("- Add lowercase letters.")

    if not re.search(r"[A-Z]", password):
        print("- Add uppercase letters.")

    if not re.search(r"[0-9]", password):
        print("- Add numbers.")

    if not re.search(r"[^a-zA-Z0-9]", password):
        print("- Add a special character.")

else:
    print("\nGreat! Your password meets all the basic requirements.")
    # Check for commonly used passwords
if password.lower() in common_passwords:
    print("\nWarning: This is a commonly used password.")