print("Hello User, Welcome to Password Strength Checker")

password = input("Enter your password: ")


if len(password) <= 7:
    print("Weak password")

elif len(password) <= 10:
     print("Medium password")
else:
     print("Strong password")
