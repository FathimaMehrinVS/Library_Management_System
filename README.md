📚 Library Management System (Python OOP)

A command-line Library Management System implemented in Python using Object-Oriented Programming (OOP) concepts.
This project allows users to add library items, register users, borrow items, return items, and calculate overdue fines.

It demonstrates important Python concepts such as:

Abstract Classes

Inheritance

Polymorphism

Exception Handling

Lists and Object Management

Date handling with datetime

🚀 Features
📖 Library Item Management

Add Books

Add Journals

Add Digital Media

Each item stores:

ID

Title

Issue Date

Issued Status

👤 User Management

Add library users

Each user maintains a list of borrowed items

🔄 Borrow Items

A user can borrow an item if:

The item exists

The item is not already issued

The item type is valid

Exceptions handled:

InvalidItemTypeException

AlreadyIssuedItemException

🔁 Return Items

Users can return borrowed items.

Fine is calculated based on item type:

Item Type	Allowed Days	Fine
Book	14 days	₹2 per extra day
Journal	7 days	₹5 per extra day
Digital Media	No fine	₹0

Exceptions handled:

NotBorrowedException

OverdueReturnException

🧠 OOP Concepts Used
1️⃣ Abstract Base Class

LibraryItem is an abstract class that defines the structure for all library items.

class LibraryItem(ABC):
    @abstractmethod
    def calculate_fine(self, return_date):
        pass
2️⃣ Inheritance

The following classes inherit from LibraryItem:

Book

Journal

DigitalMedia

Each implements its own calculate_fine() method.

3️⃣ Polymorphism

Each item type calculates fines differently using the same method:

item.calculate_fine(return_date)
4️⃣ Custom Exceptions

The system defines custom exceptions for better error handling.

InvalidItemTypeException

AlreadyIssuedItemException

NotBorrowedException

OverdueReturnException

Example:

raise OverdueReturnException("Overdue!!! Fine amount : {fine}")
📋 Menu Options

When running the program, users see the following menu:

1. Add a Book to Library
2. Add a Journal to Library
3. Add Digital Media to Library
4. Add a User
5. Borrow an Item
6. Return an Item
7. Exit
💻 Example Usage
Add a Book
Enter the book id: B101
Enter the book title: Python Programming
Book added successfully
Add a User
Enter the user id: U1
Enter the user name: Alice
User added successfully
Borrow Item
Enter the user id: U1
Enter the item id: B101

Item borrowed successfully
Return Item (with fine)

Input format for date:

YYYY,MM,DD

Example:

Enter the return date: 2026,4,8
Overdue !!! Fine amount : 34
📂 Project Structure
Library_Management_System/
│
├── library.py
└── README.md
🛠 Technologies Used

Python 3

Object-Oriented Programming

datetime module

Exception Handling

📌 Future Improvements

Possible enhancements:

Store data using files or database

Add search functionality

Add return without exception (fine payment option)

Build a GUI version (Tkinter / PyQt)

Convert to web application (Flask / Django)

👨‍💻 Author

Developed as a Python OOP practice project.