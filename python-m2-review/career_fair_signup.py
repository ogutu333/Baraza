# List to store attendees
attendees = []

# Ask the student for their details
name = input("Enter your name: ")
course = input("Enter your course: ")
mode = input("Enter your mode of learning (Part-Time or Full-Time): ")

# Add the student's name to the attendees list
attendees.append(name)

# Generate the ticket number
ticket_number = len(attendees)

# Display confirmation
print("\nThanks for signing up!")
print(f"Ticket No: {ticket_number}")
print(f"Name: {name}")
print(f"Course: {course} - {mode}")