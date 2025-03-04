Challenge: Grocery List Manager
#### Problem Statement
Create a grocery list manager where users can:
Add items with a quantity. If the item already exists, inform the user and do nothing.
Update an existing item’s quantity in the list.
Remove items from the list.
View the list in a readable format.
Exit the program when done.

#### Requirements
Store the grocery list in a dictionary, where the key is the item name and the value is the quantity.
Use a list to store menu options and display them dynamically.
Keep running until the user chooses to exit.
Input validation:
Only accept positive integers for quantities.
Prevent empty item names.
Ensure an item exists before updating or removing it.

---

Example Menu Output
Welcome to the Grocery List Manager!
Options:
1. Add Item
2. Update Item Quantity
3. Remove Item
4. View List
5. Exit
Enter your choice:


---

Core Tasks
Implement a function to display the menu dynamically based on the list.
Implement a function to add an item, ensuring it doesn’t already exist.
Implement a function to update an existing item’s quantity.
Implement a function to remove an item, ensuring it exists first.
Implement a function to view the grocery list.
Implement a function to exit the program.

---

Extra Challenge (Optional Enhancements)
Modify the program to:
Replace the menu list with a dictionary that maps menu options to functions for a cleaner structure.
Allow users to enter menu names instead of numbers (e.g., "Add Item" instead of "1").
Implement error handling for invalid inputs.
Add an option to save the grocery list to a file and load it on startup.
Allow users to clear the entire list with a new menu option.
Add an option to sort the list alphabetically before displaying.