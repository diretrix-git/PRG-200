is_logged_in = False

for _ in range(3):
    user_name = input("Enter your name: ")
    password = int(input("Enter your password: "))

    if user_name == "diretrix" and password == 6430:
        print(f"Welcome {user_name}")
        is_logged_in = True
        break

    print("Invalid entry")

if not is_logged_in:
    print("You are blocked")