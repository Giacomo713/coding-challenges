import os

class BankSystem:
    def __init__(self):
        self.account = None
        self.loginMenu = {
            "Log in": self.login,
            "Register": self.register,
            "Exit": self.exit
        }

        self.loggedMenu = {
            "Check balance": self.check_balance,
            "Deposit": self.deposit,
            "Withdraw": self.withdraw,
            "Transfer": self.transfer,
            "Log out": self.logout
        }
        self.login_menu_lower = {key.lower(): value for key, value in self.loginMenu.items()}
        self.logged_menu_lower = {key.lower(): value for key, value in self.loggedMenu.items()}

    def register(self):
        os.system('cls')
        pin = input("Enter the pin you would like to register: ")
        if not pin.isdigit() or len(pin) != 4:
            print("Pin must be a 4 digit value")

        elif os.path.exists(f"{pin}.txt"):
            print("User already registered")
        else:
            f = open(f"{pin}.txt", "x")
            f.write("0.00")
            print("Successfully registered")

    def login(self):
        os.system('cls')
        pin = input("Enter your pin: ")
        if not os.path.exists(f"{pin}.txt"):
            print("User does not exist")

        else:
            print("Login successful")
            f = open(f"{pin}.txt", "r")
            self.account = UserAccount(pin, f.read())

    def check_balance(self):
        os.system('cls')
        balance = f"{self.account.balance:,.2f}"
        print(f"Your current balance is: €{balance}")

    def deposit(self):
        os.system('cls')
        amount = float(input("Enter the amount you would like to deposit: "))
        if amount > 0:
            self.account.deposit(amount)
            self.account.save()
        else:
            print("Please enter a positive amount to deposit")

    def withdraw(self):
        os.system('cls')
        amount = float(input("Enter the amount you would like to withdraw: "))
        if amount > 0:
            self.account.withdraw(amount)
            self.account.save()
        else:
            print("Please input a positive amount to withdraw")

    def transfer(self):
        os.system('cls')
        balance = f"{self.account.balance:,}"
        receiver = input("Input the destination account: ")
        amount = float(input(f"Input the amount of money you would like to send, it must be less than your current balance(€{balance}): "))
        self.account.balance -= amount
        self.account.save()
        if amount > 0:
            try:
                f = open(f"{receiver}.txt", "r")
                tmp = float(f.read()) + amount
                f = open(f"{receiver}.txt", "w")
                f.write(str(tmp))
            except FileNotFoundError:
                print("Destination account doesnt exist!")
        else:
            print("Please input a positive amount to transfer")

    def main(self):
        os.system('cls')
        while True:
            if self.account is None:
                print("Welcome to PythonBank!")
                for index, item in enumerate(self.loginMenu):
                    print(f"{[index + 1]} {item}")
                usrChoice = input("Select your option: ").lower()
                if usrChoice in self.login_menu_lower.keys():
                    self.login_menu_lower[usrChoice]()
                else:
                    try:
                        menu_option = list(self.loginMenu.values())[int(usrChoice) - 1]
                        menu_option()
                    except ValueError:
                        os.system('cls')
                        print("Please input a valid menu selection.")
            else:
                try:
                    for index, item in enumerate(self.loggedMenu):
                        print(f"{[index + 1]} {item}")
                    usrChoice = input("Select your option: ").lower()
                    self.logged_menu_lower[usrChoice]()
                except KeyError:
                    try:
                        menu_option = list(self.loggedMenu.values())[int(usrChoice) - 1]
                        menu_option()
                    except ValueError:
                        os.system('cls')
                        print("Please input a valid menu selection.")

    def logout(self):
        os.system('cls')
        self.account = None

    def exit(self):
        exit()

class UserAccount:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)

    def withdraw(self, amount):
        if self.balance >= float(amount):
            self.balance -= float(amount)
        else:
            print("Value you entered is greater than the amount of money present in your bank account!")

    def save(self):
        f = open(f"{self.pin}.txt", "w")
        f.write(str(self.balance))

BankSystem().main()