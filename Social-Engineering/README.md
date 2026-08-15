# Password Strength Checker 🔐

## Overview

This lab focused on creating a simple **Python password strength checker**. The aim was to build a script that checks whether a password follows basic cybersecurity best practices and gives the user recommendations when it is weak.

This was useful for understanding how weak passwords can increase security risks and how Python can be used to automate basic security checks.

## Objectives

The script was designed to:

- Check the length of a password.
- Check for both uppercase and lowercase letters.
- Check for numbers and special characters.
- Identify common passwords.
- Prevent the user from submitting an empty password.
- Give feedback and recommendations for improving weak passwords.
- Combine all the checks to determine whether the password is strong or weak.

## Technologies Used

- **Python 3**
- Python built-in functions
- `any()`
- `len()`
- String methods such as `isupper()`, `islower()`, `isdigit()`, and `isalnum()`
- `while` loops
- Functions and conditional statements

## Lab Tasks

### Task 1 — Determine Scope and Functionality

Before writing or changing the code, I reviewed what the script needed to do.

The main requirements were to check:

1. Password length
2. Character variety
3. Common passwords
4. Overall password strength
5. Recommendations for weak passwords

### Task 2 — Add Password Checking Functions

I created separate functions for each password characteristic:

- `check_length()` — checks whether the password contains at least 8 characters.
- `check_case()` — checks for uppercase and lowercase letters.
- `check_numbers_special()` — checks for numbers and special characters.
- `check_common_passwords()` — checks whether the password matches a list of common passwords.

Breaking the checks into separate functions made the script easier to understand and maintain.

### Task 3 — User Input Validation

A `while` loop was added to make sure the user cannot submit an empty password.

If the input is empty, the script displays:

> Password cannot be empty. Please try again.

The user is then asked to enter a password again.

### Task 4 — Integrate the Functions

The `check_password_strength()` function calls all four checking functions and collects their results.

If every check passes, the script reports:

> Strong password! Good job.

If one or more checks fail, the script reports that the password is weak and displays recommendations for improvement.

### Task 5 — Feedback and Recommendations

The script provides specific feedback depending on which checks fail.

For example, a weak password might receive recommendations such as:

- Use at least 8 characters.
- Add both uppercase and lowercase letters.
- Add at least one number and one special character.
- Do not use a common password.

## Example

### Strong Password

```text
Enter a password: CyberLab@2026

Strong password! Good job.
```

### Weak Password

```text
Enter a password: password

Weak password. Recommendations:
Use at least 8 characters.
Add both uppercase and lowercase letters.
Add at least one number and one special character.
Do not use a common password.
```

# Key Cybersecurity Concepts Learned

### Password Security

Weak and reused passwords can make it easier for attackers to gain unauthorised access to accounts and systems. Password policies should encourage users to create passwords that are difficult to guess.

### Password Complexity

The script checks for different character types instead of only checking the password length. This demonstrates how password policies can enforce minimum security requirements.

### Common Passwords

Passwords such as `password`, `123456`, and `qwerty` are easy to guess and should be avoided. Checking against known common passwords is one way of identifying obvious weaknesses.

### Input Validation

The script also validates user input before processing it. This prevents an empty value from being accepted.

### Python Functions

Using separate functions for each security check made the program more modular. Each function has one main responsibility, which makes the code easier to test and modify.

## What I Learned

This lab helped me understand how simple Python scripts can be applied to cybersecurity problems. I also got more practice with functions, loops, conditions, string methods, and user input.

One thing I learned is that password strength is based on more than just length. Character variety and avoiding common passwords are also important.

## Limitations

This is a basic educational password checker and should not be treated as a complete password security solution.

Some limitations include:

- The common password list is very small.
- It does not check against large breached-password databases.
- It does not measure password entropy.
- It does not detect predictable patterns such as `Password123!`.
- The minimum length is set to 8 characters, which is only a basic requirement.

For a real organisation, the checker would need a much larger password database and stronger password security controls.

## Possible Improvements

If I continued developing this project, I could:

- Add a larger list of commonly used passwords.
- Check passwords against known breached-password databases.
- Add a password strength score.
- Detect repeated or predictable characters.
- Add a graphical or web interface.
- Allow organisations to define their own password policies.
- Add unit tests for each function.

## Security+ Connection

This lab relates to **CompTIA Security+** topics around:

- Authentication
- Password policies
- Access control
- Account security
- Security best practices
- Preventing unauthorised access

It also demonstrates how basic scripting can be used to automate security tasks.

## Conclusion

Overall, this lab gave me practical experience using Python for a basic cybersecurity task. I created a password checker that evaluates several password characteristics and gives users useful recommendations.

It also showed me how small security controls, such as enforcing stronger passwords, can help reduce the risk of unauthorised access.