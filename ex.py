users = []

print(" WELCOME TO PYTHON BANK")

# --- Added Functions ---
def view_balance(user):
    print("Current Balance:", user["Balance"])

def deposit(user):
    try:
        amount = int(input("Enter Deposit Amount: "))
        if amount > 0:
            user["Balance"] += amount
            print("Amount Deposited Successfully")
            print("New Balance:", user["Balance"])
        else:
            print("Deposit amount must be positive!")
    except ValueError:
        print("Invalid input! Please enter a number.")

def withdraw(user):
    try:
        amount = int(input("Enter Withdrawal Amount: "))
        if amount > 0:
            if amount <= user["Balance"]:
                user["Balance"] -= amount
                print("Amount Withdrawn Successfully")
                print("New Balance:", user["Balance"])
            else:
                print("Insufficient Balance!")
        else:
            print("Withdrawal amount must be positive!")
    except ValueError:
        print("Invalid input! Please enter a number.")

# --- Main Program ---
while True:
    print("\n1. Sign Up")
    print("2. Sign In")
    print("3. Exit")

    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    match choice:

        case 1:
            user = {}

            print("\n SIGN UP")
            user["Name"] = input("Enter Name: ").strip()
            user["Username"] = input("Enter Username: ").strip().lower()
            user["Email"] = input("Enter Email: ").strip()
            user["Password"] = input("Enter Password: ").strip().lower()

            try:
                user["Balance"] = int(input("Enter Initial Balance: "))
            except ValueError:
                print("Invalid input! Balance must be a number.")
                continue

            users.append(user)

            print("\nAccount Created Successfully!")
            print("Welcome to Python Bank,", user["Name"])

        case 2:
            print("\n SIGN IN")

            username = input("Enter Username: ").strip().lower()
            password = input("Enter Password: ").strip().lower()

            for user in users:

                if user["Username"] == username and user["Password"] == password:

                    print("\nLogin Successful!")
                    print("Welcome Back,", user["Name"])

                    while True:
                        print("\n BANK MENU ")
                        print("1. View Balance")
                        print("2. Deposit")
                        print("3. Withdraw")
                        print("4. Logout")

                        try:
                            choice = int(input("Choose an option: "))
                        except ValueError:
                            print("Invalid input! Please enter a number.")
                            continue

                        match choice:

                            case 1:
                                view_balance(user)

                            case 2:
                                deposit(user)

                            case 3:
                                withdraw(user)

                            case 4:
                                print("Logged Out Successfully!")
                                break

                            case _:
                                print("Invalid Choice!")

                    break

            else:
                print("Invalid Username or Password!")

        case 3:
            print("Thank You For Using Python Bank")
            break

        case _:
            print("Invalid Choice!")