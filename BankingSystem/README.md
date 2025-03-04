Challenge: Simple Banking System (OOP & File Handling)
#### Problem Statement
Create a simple banking system using OOP where users can:
Register with a unique 4-digit PIN (stored in a file).
Log in using their PIN and access their account.
Check their balance (formatted properly in euros).
Deposit money (fake money, updates immediately).
Transfer money to another registered user (if they exist).
Log out and return to the login screen.

---

Requirements
#### 1. Use Existing Knowledge
Dictionaries mapped to functions for menus.
File handling for data persistence.
Exception handling for input validation.
Looping structures for repeated interactions.

#### 2. Object-Oriented Structure
UserAccount class: Handles balance updates (deposit, transfer).
BankSystem class: Manages user registration, login, and file handling.

#### 3. User Authentication
Users register with a unique 4-digit PIN.
Each PIN is linked to {pin}.txt storing the balance.
Login requires entering a valid registered PIN.

#### 4. Banking Operations
Check Balance → Display balance in euros (€) (e.g., €1,234.56).
Deposit Money → Add any positive amount (including cents).
Transfer Money →
Enter recipient’s PIN.
Sender’s balance must not go negative.
Recipient’s balance updates immediately.
Logout → Return to login screen (balances already saved).

#### 5. File Handling
Each user’s balance is stored in {pin}.txt.
Balances must be updated in real time.

#### 6. Exception Handling
PIN validation → Must be 4 digits, numeric.
Amount validation → Must be a positive number (e.g., 10.50 is valid).
Transfers → Cannot exceed available balance.
File safety → Ensure files exist before reading.

---

Example Menu Output
Welcome to Simple Banking System!
1. Register
2. Login
Enter your choice: _

Enter your 4-digit PIN: 1234
Login successful!
---------------------------
1. Check Balance
2. Deposit Money
3. Transfer Money
4. Logout
Enter your choice: _


---

Core Tasks
Implement the UserAccount class for balance updates.
Implement the BankSystem class for login, registration, and file handling.
Use a dictionary-based menu system.
Implement balance checking (formatted in euros).
Implement depositing money (updates immediately).
Implement transferring money (validate recipient and amount).
Implement logging out (return to login screen).

---

Extra Challenge (Optional Enhancements)
#### 1. Transaction Logging
Log all transactions in transactions.log:
[YYYY-MM-DD HH:MM] PIN 1234 -> Deposit €50.00
Allow users to view their last 5 transactions.

#### 2. SQLite3 Database (Instead of Text Files)
Store user accounts and balances in bank.db.
Store transactions in a separate table instead of a log file.