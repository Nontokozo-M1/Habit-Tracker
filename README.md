# Habit Tracker

## 1. About the Project
This project is a Habit Tracker developed using Python. It allows users to create habits, record when they complete them and keep track of their progress.
The application supports daily and weekly habits. It also allows users to analyse their habits by viewing their longest completion streaks.

---
## 2. Main Features
The application allows users to:
- Create new daily or weekly habits.
- Delete habits they no longer want to track.
- Mark habits as completed.
- View all saved habits.
- Filter habits according to their frequency.
- Find the longest streak across all habits.
- Find the longest streak for a specific habit.
- Save and load habit information using a JSON file.
  
---
## 3. Project Files

The project contains the following files:

- `habit_tracker.py` – Contains the Habit class and the functions used by the application.
- `Habits_Tracker.ipynb` – Contains the main application menu.
- `Example_Data.ipynb` – Contains five predefined habits and their example completion records.
- `Unit_Tests.ipynb` – Contains nine unit tests used to check the application's functions.
- `habits_app.json` – Stores the habit information.
- `README.md` – Provides information about the project and how to use it.
  
---
## 4. Requirements
To run the application, you need:
- Python
- Jupyter Notebook
The project also uses Python's built-in `json` and `datetime` modules.
`habit_tracker.py` must be in the same project folder as the main notebook.

---
## 5. How to Run the Application
1. Make sure `habit_tracker.py` is in the same project folder as the notebook.
2. Open `Habits_Tracker.ipynb` in Jupyter Notebook.
3. Run the import cell.
4. Run the cell containing the main menu.
5. Choose an option from the menu and follow the instructions.
6. Select option 5 to exit.
  
---
## 6. Example Data
The `Example_Data.ipynb` notebook contains five sample habits with completion records covering four weeks.

These are the five example habits:
- Exercise – Daily
- Read – Daily
- Drink water – Daily
- Clean room – Weekly
- Plan weekly budget – Weekly

**Note:** Running the example data cell replaces the existing data in `habits_app.json` with the five predefined habits.
  
---
## 7. Testing
To run the tests:

1. Open `Unit_Tests.ipynb` in Jupyter Notebook.
2. Run the import cell to access the functions from `habit_tracker.py`.
3. Run the unit test cell.

All nine tests should pass if the application functions are working correctly.

---
## 8. Saving Data
Habit information is stored in `habits_app.json`. This allows the application to load previously saved habits when it is opened again.

The file is updated when habits are created, deleted or marked as completed.