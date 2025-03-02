import os

grocery_list = {}

f = open("grocery_list.txt", "r")
if os.path.exists("grocery_list.txt"):
    for items in f.read().splitlines():
        keys = items.split(":")
        grocery_list[keys[0]] = keys[1]

def grocery_inserter(grocery_list):
    os.system('cls')
    item = input("Enter the item you want to add to the list: ").lower().strip()
    quantity = int(input("Enter the amount of the item you want to add: "))
    if item not in grocery_list.keys():
        grocery_list[item] = quantity
        os.system('cls')
        print(f"item '{item}' has been added to the list.")
    else:
        print(f"Item {item} is already present in the grocery list with a quantity of {grocery_list[item]}")

def grocery_updater(grocery_list):
    os.system('cls')
    print("\nThe grocery list currently has the following items:")
    for item, quantity in grocery_list.items():
        print(f"'{item}' with a quantity of: {quantity}")
    item = input("Enter the name item you want to update: ").lower()
    quantity = int(input("Enter the updated quantity: "))
    if quantity > 0 and item in grocery_list.keys():
        grocery_list[item] = quantity
        os.system('cls')
        print(f"Item '{item}' has been updated to quantity: {quantity}")
    else:
        print("\nPlease make sure the item you introduced is in the grocery list and the quantity you introduced is greater than 0.")
        grocery_updater(grocery_list)
    print(grocery_list)

def grocery_remover(grocery_list):
    os.system('cls')
    print("The grocery list currently has the following items:")
    for item, quantity in grocery_list.items():
        print(f"'{item}' with a quantity of: {quantity}")
    item = input("\nPlease enter the name of the item you want to remove: ")
    if item in grocery_list.keys():
        del grocery_list[item]
        os.system('cls')
        print("\nSuccessfully removed the item from the grocery list.")
    else:
        print("\nThe item you introduced is not present in the grocery list.")
        grocery_remover(grocery_list)

def grocery_viewer(grocery_list):
    os.system('cls')
    print("The grocery list currently has the following items:")
    for item, quantity in grocery_list.items():
        print(f"'{item}' with a quantity of: {quantity}")
    input("Input anything to return to the menu.")
    os.system('cls')

def save_list(grocery_list):
    f = open("grocery_list.txt", "w")
    grocery_items = ""
    for item, quantity in grocery_list.items():
        grocery_items += f"{item}:{quantity}\n"
    f.write(grocery_items)

def clear_list(grocery_list):
    grocery_list = {}
    os.remove("grocery_list.txt")
    f = open("grocery_list.txt", "w")

def stop_list(grocery_list):
    exit()

menu_options = {"Add item": grocery_inserter,
                "Update item": grocery_updater,
                "Remove item": grocery_remover,
                "View list": grocery_viewer,
                "Save list": save_list,
                "Clear list": clear_list,
                "Exit": stop_list,
                }

menu_options_lower = {key.lower(): value for key, value in menu_options.items()}

while True:
    print("\nWelcome to Grocery List Manager")
    for index, option in enumerate(menu_options):
        print(f"{index + 1}. {option}")
    usr_choice = input("Input your choice: ").lower()
    if usr_choice in menu_options_lower.keys():
        print(menu_options_lower[usr_choice](grocery_list))
    else:
        try:
            menu_option = list(menu_options.values())[int(usr_choice) - 1]
            menu_option(grocery_list)
        except IndexError:
            print(f"input a valid number range (1 - {len(menu_options)})")
        except ValueError:
            print("Please, try again")