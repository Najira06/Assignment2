count=0
while count < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username=="najira" and password=="amin":
        print("Access granted")
        break
    else:
        print("Access denied. Try again.")
        count += 1