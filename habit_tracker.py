import json
from datetime import datetime, timedelta


class Habit:
    """Represent a habit and store its completion history."""

    def __init__(self, habit_name, periodicity):
        self.habit_name = habit_name
        self.periodicity = periodicity
        self.create_time = datetime.now()
        self.completed_dates = []

    def check_off(self):
        """Record the current date and time when a habit is completed."""
        completed_time = datetime.now()
        self.completed_dates.append(completed_time)
        print("Habit completion successfully recorded!")
        return completed_time


def get_all_habits(habits):
    """Return all habits in the list."""
    return habits


def get_habits_by_periodicity(habits, periodicity):
    """Return habits that match the given periodicity."""
    matching_habits = []
    for habit in habits:
        if habit.periodicity == periodicity:
            matching_habits.append(habit)
    return matching_habits


def get_habit_longest_streak(habit):
    """Calculate the longest consecutive streak for one habit."""
    if habit.periodicity == "daily":
        sorted_dates = sorted(set(date.date() for date in habit.completed_dates))

    elif habit.periodicity == "weekly":
        sorted_dates = sorted(set(
            date.date() - timedelta(days=date.weekday())
            for date in habit.completed_dates
        ))

    if not sorted_dates:
        return 0

    if habit.periodicity == "daily":
        required_difference = timedelta(days=1)

    elif habit.periodicity == "weekly":
        required_difference = timedelta(weeks=1)

    current_streak = 1
    longest_streak = 1

    for i in range(1, len(sorted_dates)):
        difference = sorted_dates[i] - sorted_dates[i-1]

        if difference == required_difference:
            current_streak += 1
        else:
            current_streak = 1

        if current_streak > longest_streak:
            longest_streak = current_streak

    return longest_streak


def get_longest_streak(habits):
    """Find the longest streak across all habits."""
    longest_streak = 0

    for habit in habits:
        habit_streak = get_habit_longest_streak(habit)

        if habit_streak > longest_streak:
            longest_streak = habit_streak

    return longest_streak


def save_habits(habits):
    """Save the habits and their completion history to a JSON file."""
    all_habit_data = []

    for habit in habits:
        completed_dates_data = []

        for date in habit.completed_dates:
            converted_date = date.isoformat()
            completed_dates_data.append(converted_date)

        habit_data = {
            "habit_name": habit.habit_name,
            "periodicity": habit.periodicity,
            "create_time": habit.create_time.isoformat(),
            "completed_dates": completed_dates_data
        }

        all_habit_data.append(habit_data)

    with open("habits_app.json", "w") as f:
        json.dump(all_habit_data, f)


def create_habit_from_data(habit_data):
    """Create a Habit object from previously saved JSON data."""
    loaded_habit = Habit(
        habit_data["habit_name"],
        habit_data["periodicity"]
    )

    loaded_habit.create_time = datetime.fromisoformat(
        habit_data["create_time"]
    )

    completed_dates = []

    for date in habit_data["completed_dates"]:
        converted_date = datetime.fromisoformat(date)
        completed_dates.append(converted_date)

    loaded_habit.completed_dates = completed_dates

    return loaded_habit


def load_habits():
    """Load saved habits from the JSON file."""
    try:
        with open("habits_app.json", "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        data = []

    loaded_habits = []

    for habit_data in data:
        loaded_habit = create_habit_from_data(habit_data)
        loaded_habits.append(loaded_habit)

    return loaded_habits


def delete_habit(habits, habit_name):
    """Delete a habit by name and return whether it was found."""
    habit_found = False

    for habit in habits:
        if habit.habit_name.lower() == habit_name.lower():
            habits.remove(habit)
            habit_found = True
            break

    if habit_found:
        print("Habit deleted successfully!")
    else:
        print("Habit not found. Please try again.")

    return habit_found