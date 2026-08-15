# Password Strength Checker

def check_length(password):
    """Checks if the password is at least 8 characters long."""
    if len(password) >= 8:
        return True, "Password length is good."
    else:
        return False, "Use at least 8 characters."


def check_case(password):
    """Checks for uppercase and lowercase letters."""
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if has_upper and has_lower:
        return True, "Password has uppercase and lowercase letters."
    else:
        return False, "Add both uppercase and lowercase letters."


def check_numbers_special(password):
    """Checks for numbers and special characters."""
    has_number = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if has_number and has_special:
        return True, "Password has numbers and special characters."
    else:
        return False, "Add at least one number and one special character."


def check_common_passwords(password):
    """Checks if the password is a common password."""
    common_passwords = [
        "password",
        "123456",
        "123456789",
        "qwerty",
        "admin",
        "letmein"
    ]

    if password.lower() in common_passwords:
        return False, "Do not use a common password."
    else:
        return True, "Password is not a common password."


def check_password_strength(password):
    """Evaluates the password using all checks and returns feedback."""
    results = []

    # Call each function and collect feedback
    length_ok, length_msg = check_length(password)
    case_ok, case_msg = check_case(password)
    num_spec_ok, num_spec_msg = check_numbers_special(password)
    common_ok, common_msg = check_common_passwords(password)

    results.append(length_msg)
    results.append(case_msg)
    results.append(num_spec_msg)
    results.append(common_msg)

    # Determine overall strength
    if all([length_ok, case_ok, num_spec_ok, common_ok]):
        return "Strong password! Good job."
    else:
        return "Weak password. Recommendations:\n" + "\n".join(results)


# User input and validation
while True:
    password = input("Enter a password: ")
    if password.strip() == "":
        print("Password cannot be empty. Please try again.")
    else:
        break

# Display the results
print(check_password_strength(password))