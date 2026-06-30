# Python Practice Quiz 1: M2 Review

This project contains solutions to a Python practice quiz covering fundamental programming concepts including data types, variables, operators, built-in functions, loops, functions, and conditional statements. Each question is designed to reinforce core programming skills through practical, real-world scenarios.

## Concepts Covered

- **Data Types & Variables:** String, integer, list, and dictionary manipulation
- **Operators & Keywords:** and, or, is, is not, in, not in
- **Built-in Functions**: print(), input(), int(), str(), len()
- **Loops**: for and while loops with range and list iteration
- **Functions**: Defining functions with parameters and arguments
- **Conditionals**: if, else, and nested if-else statements

---

## Exercises

### Question 1: Career Fair Sign-up System
**Goal**: Create a student registration system for a career fair.

**Features**:
- Collects student name, course, and learning mode (part-time/full-time)
- Stores attendee information
- Generates a ticket number
- Displays a registration confirmation

**Skills Practiced**: Variables, user input, list operations, string formatting

---

### Question 2: Password Strength Checker
**Goal**: Validate password security with detailed feedback.

**Validation Rules**
- Minimum of 8 characters
- At least one uppercase letter
- At least one number
- At least one special character (`@ # $ % ^ & *`)

**Features**: 
- Provides specific feedback for each criterion 
- Counts the number of uppercase letters, digits, and special characters

**Skills Practiced**: String methods, character iteration, conditional statements, counting techniques

---

### Question 3: Number Guessing Game
**Goal**: Create an interactive guessing game with limited attempts.

**Features**
- Asks for player's name at start 
- Allows 3 attempts to guess a predetermined lucky number 
- Provides feedback after each incorrect attempt 
- Congratulates the player on success or ends after 3 failures

**Skills Practiced**: Loops with break statements, user input, conditional logic, game mechanics

---

### Question 4: WiFi Credential System
**Goal**: Implement a department-based WiFi credential retrieval system.

**Features**
- Differentiates between staff and guest users 
- Staff members provide department (Finance, Marketing, IT, Operations) 
- Retrieves department-specific SSID and password 
- Guests verify front desk sign-in before receiving credentials 
- Handles invalid inputs with appropriate error messages

**Skills Practiced**: Nested conditionals, dictionary-like data access, input validation

---

### Question 5: Security Log Analyzer
**Goal**: Analyze system logs to detect potential brute-force attacks.

**Features**
- Parses log entries containing IP addresses and login status 
- Tracks failed login attempts per IP address 
- Triggers an alert when any IP has 3 or more failed logins 
- Stops analysis upon detection

**Skills Practiced**: List iteration, string parsing, dictionary for tracking counts, break statements

---

### Question 6: Port Scanner Function
**Goal**: Create a reusable function for network port scanning.

**Features**
- User-defined function with start and end port parameters 
- Iterates through the specified port range 
- Simulates port scanning by printing each port number

**Skills Practiced**: Function definition, parameters, range-based iteration, print formatting

---

## Getting Started

### Prerequisites

- Python 3.x
- A code editor or IDE such as:
  - Visual Studio Code
  - PyCharm
  - IDLE

### Running the Programs

Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
```

Navigate into the project directory:

```bash
cd python-m2-review
```

Run any exercise using Python:

```bash
python filename.py
```

Replace `filename.py` with the name of the exercise you want to run.

---

## Learning Outcomes

By completing these exercises, I was be able to:

- Write Python programs that interact with users through input/output 
- Implement conditional logic to handle various scenarios 
- Create and manipulate lists, dictionaries, and strings 
- Write functions with parameters and return values 
- Apply loops for repetitive tasks 
- Validate user input and provide appropriate feedback

---

## Project Structure

```text
python-m2-review/
│
├── career_fair_signup.py
├── password_checker.py
├── guessing_game.py
├── wifi_questionnaire.py
├── brute_force_detector.py
├── port_scanner.py
└── README.md
```

---

## License

This project is provided for educational purposes at Moringa School.