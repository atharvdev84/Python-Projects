# 💰 Expense Tracker

📊 A command-line expense management application built with Python that helps users record, organize, analyze, and manage daily expenses using persistent JSON storage.

## ✨ Features

- ➕ Add new expenses
- 👀 View all recorded expenses
- 💰 Calculate total expenses
- 📂 Categorize expenses
- 📅 Store expense dates
- 🔥 Identify the most used expense category
- ✏️ Edit existing expense records
- ❌ Remove unwanted expense entries
- 💾 Persistent JSON data storage
- 🛡️ Input validation and error handling
- 📂 Modular multi-file architecture

## 📸 Preview

```text
1. Add Expense
2. View Expense
3. Exit
4. Total Expense
5. Most Used Category
6. Remove
7. Edit List

Enter choice: 1

Enter amount: 500
Enter category: Food
Enter year: 2025
Enter month: 6
Enter day: 20

Expense Added Successfully
```

## 🛠️ Technologies Used

- 🐍 Python
- 📄 JSON
- 📅 Datetime Module
- 📂 File Handling

## 📁 Project Structure

```text
expense_tracker/
│
├── input.py      # Main menu and user interaction
├── main.py       # Expense creation and data collection
├── view.py       # Expense viewing and analytics
├── remove.py     # Edit and delete functionality
├── save.py       # JSON storage operations
└── data.json     # Expense database
```

## 📚 What I Learned

- Working with JSON databases
- Reading and writing structured data
- Modular programming
- Organizing projects across multiple files
- Lists and dictionaries
- Exception handling
- Input validation
- CRUD operations
- Data analysis using Python
- Date handling with the Datetime module

## 📊 Analytics Features

The application provides useful spending insights by:

- Calculating total money spent across all records
- Tracking spending categories
- Finding the most frequently used expense category
- Organizing expenses with date information

## 🚀 Project Overview

This project was built to simulate a real-world expense management system. Users can record expenses with categories and dates, view stored records, edit existing entries, remove unwanted data, and analyze spending patterns. All information is stored in a JSON file, allowing expense data to persist between sessions.

Compared to beginner Python projects, this application introduces modular design, persistent data storage, data analysis, and complete CRUD functionality, making it a strong intermediate-level project.
