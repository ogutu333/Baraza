# Ask if the user is staff or a guest
user_type = input("Are you staff or a guest? ")

if user_type.lower() == "staff":
    department = input("Which department do you work in? ")

    if department.lower() == "finance":
        print("WiFi Name: Corp_Finance_Secure")
        print("Password: Fi$n4nc3!99#")

    elif department.lower() == "marketing":
        print("WiFi Name: Corp_Marketing_Secure")
        print("Password: Mktg*Grow!2026")

    elif department.lower() == "it":
        print("WiFi Name: Corp_IT_Secure")
        print("Password: 1T_D3v_@ccess!")

    elif department.lower() == "operations":
        print("WiFi Name: Corp_Operations_Secure")
        print("Password: 0p3r4ti0n5_W1f1")

    else:
        print("Department not recognized, add a valid department name.")

elif user_type.lower() == "guest":
    signed_in = input("Have you signed in at the front desk? (yes/no) ")

    if signed_in.lower() == "yes":
        print("WiFi Name: Corp_Guests")
        print("Password: WelcomeToCorp2026")
    else:
        print("Please go sign in first.")

else:
    print("Please enter either staff or guest.")