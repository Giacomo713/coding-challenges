import os

LoggedIn = False

class BankSystem:
    def __init__(self):
        self.account = None
        self.loginMenu = {
            "Log in": self.login,
            "Register": self.register
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
        pin = input("Enter your pin")
        if not pin.isdigit() and len(pin) != 4:
            print("Pin must be a 4 digit value")

        if os.path.exists(f"{pin}.txt"):
            print("User already registered")
        else:
            f = open(f"{pin}.txt", "x")
            f.write("0")
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
        print(f"Your current balance is: {self.account.balance}")

    def deposit(self):
        os.system('cls')
        amount = input("Enter the amount you would like to deposit: ")
        self.account.deposit(amount)
        self.account.save()
    def withdraw(self):
        os.system('cls')
        amount = int(input("Enter the amount you would like to withdraw: "))
        self.account.withdraw(amount)
        self.account.save()

    def transfer(self):
        os.system('cls')
        receiver = input("Input the destination account: ")
        amount = int(input(f"Input the amount of money you would like to send, it must be less than your current balance({self.account.balance}): "))
        self.account.balance -= amount
        self.account.save()
        f = open(f"{receiver}.txt", "r")
        tmp = int(f.read()) + amount
        f = open(f"{receiver}.txt", "w")
        f.write(str(tmp))

    def main(self):
        os.system('cls')
        while True:
            if self.account is None:
                print("welcome to bank")
                for index, item in enumerate(self.loginMenu):
                    print(f"{[index + 1]} {item}")
                usrChoice = input("Select your option: ").lower()
                if usrChoice in self.login_menu_lower.keys():
                    self.login_menu_lower[usrChoice]()
                else:
                    menu_option = list(self.loginMenu.values())[int(usrChoice) - 1]
                    menu_option()
            else:
                try:
                    for index, item in enumerate(self.loggedMenu):
                        print(f"{[index + 1]} {item}")
                    usrChoice = input("Select your option: ").lower()
                    self.logged_menu_lower[usrChoice]()
                except:
                    menu_option = list(self.loggedMenu.values())[int(usrChoice) - 1]
                    menu_option()

    def logout(self):
        os.system('cls')
        self.account = None

class UserAccount:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = int(balance)

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def save(self):
        f = open(f"{self.pin}.txt", "w")
        f.write(str(self.balance))

BankSystem().main()