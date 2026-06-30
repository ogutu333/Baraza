# Ask the user to enter a password
password = input("Enter your password: ")

# Check the length
if len(password) >= 8:
    print("Length is OK -", len(password), "characters")
else:
    print("Length is NOT OK - Only", len(password), "characters")

# Count uppercase letters
uppercase = 0
for character in password:
    if character.isupper():
        uppercase += 1

if uppercase > 0:
    print("Letter case is OK - has", uppercase, "uppercase letter(s)")
else:
    print("Letter case is NOT OK - has no uppercase characters")

# Count numbers
numbers = 0
for character in password:
    if character.isdigit():
        numbers += 1

if numbers > 0:
    print("Presence of numbers is OK - has", numbers, "number(s)")
else:
    print("Presence of numbers is NOT OK - has no numbers")

# Count special characters
special = 0
special_characters = "@#$%^&*"

for character in password:
    if character in special_characters:
        special += 1

if special > 0:
    print("Presence of special characters is OK - has", special, "special character(s)")
else:
    print("Presence of special characters is NOT OK - has no special characters")