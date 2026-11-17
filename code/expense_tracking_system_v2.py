# ===============================================================
# EXPENSE TRACKER SYSTEM
# ===============================
# This is a newer attempt but from asking AI to give me a task.
# Since watching CS50P, I have incorporated some of my learnings such as creating a main().

# This is the requirements I got from the ai:

# Core requirements
# -------------------------------
# Show a menu with options: add expense, view all expenses, show summary, quit.
# Add expense: ask for an amount, a category (e.g. food, transport, fun) and a short description. Reject amounts that are negative or aren’t numbers, and ask again.
# View all: print every expense in a neat table with the date it was added.
# Summary: show the total spent, the total for each category, and the biggest single expense.
# Save to a file (CSV or JSON) so expenses are still there the next time you run the program.

# What I learned
# -------------------------------
# I feel like since my first one, I have improved again. 
# I need to learn with / open, so I can begin writing and reading files too.
# I am very happy with this. I know in 6 months from now I might cringe, but for now it works and I designed many functions.
# I also incorporated try and except too.
#
# ===============================================================



# Modules
# -------------------------------
import sys
from tabulate import tabulate


# -------------------------------
# MAIN
# -------------------------------
def main():

    # Title
    print(title("expense tracker"))

    # Copy
    print("Welcome to the expense tracker.")
    print("A system built to track expenses\n")

    while True:
        # Menu
        print(menu_heading("menu"))
        print("1 – Add an Expense.")
        print("2 – View All Expenses.")
        print("3 – Show Summary.")
        print("4 – Exit.\n")

        # Users Input
        user_request(get_answer())


# -------------------------------
# Expenses Tracker Database
# -------------------------------
expenses = [
    {"amount": 3, "category": "transport", "description": "bus"},
    {"amount": 5, "category": "food", "description": "lunch"},
    {"amount": 12.5, "category": "transport", "description": "train"},
]

# -------------------------------
# Get Expense Functions
# -------------------------------

def get_expense_amount() -> float:
    """
    Asks the user to input the expense amount.

    Args:
        None
    Returns:
        expense_amount (float): The expense amount.
    Raises:
        ValueError: If the user doesn't input a correct amount.
        ValueError: If the amount is not greater than 0.
    """
    while True:
        try:
            expense_amount = float(input("Enter the expense amount here:\n"))
            if expense_amount > 0:
                return expense_amount
            else:
                print("\nThe amount must be greater than 0")
        except ValueError:
            print("\nThe amount needs to be in digits")

def get_expense_category() -> str:
    """
    Asks the user to input the expense category.
    The function then cleans the text and makes it lowercase.
    Args:
        None
    Returns:
        expense_category_cleaned (str): The expense category.
    """
    expense_category_raw = input("\nEnter the expense category here:\n")
    expense_category_cleaned = expense_category_raw.strip().lower()
    return expense_category_cleaned

def get_expense_description() -> str:
    """
    Asks the user to input the expense description.
    The function then cleans the text and makes it lowercase.
    Args:
        None
    Returns:
        expense_description_cleaned (str): The expense description.
    """
    expense_description_raw = input("\nEnter a short description for the expense:\n")
    expense_description_cleaned = expense_description_raw.strip().lower()
    return expense_description_cleaned

def get_expense() -> dict:
    """
    Gets an expense from the user.

    Calls:
        get_expense_amount(),
        get_expense_category(),
        get_expense_description()
    Returns:
        expense (dict): A dict of the expense.
    """
    expense_amount = get_expense_amount()
    expense_category = get_expense_category()
    expense_description = get_expense_description()

    expense = {
        "amount" : expense_amount,
        "category" : expense_category,
        "description" : expense_description
    }
    return expense
# -------------------------------
# Add Expense Function
# -------------------------------
def add_expense(expense: dict) -> str:
    """
    Adds an expense to the expenses database.

    Args:
        expense (dict): The dictionary of the expense.
    Returns:
        (str): A note to say the expense has been added.
    """
    expenses.append(expense)
    return "Expense has been added!"

# -------------------------------
# View All Expenses Function
# -------------------------------
def show_expenses() -> None:
    """
    Shows all the expenses as a neat table.

    Returns:
        None.
    """
    print(make_table(expenses))

# -------------------------------
# Summary Functions
# -------------------------------
def get_total() -> float:
    """
    Gets the total of all the expenses.

    Returns:
        total (float): The grand total of all the expenses.
    """
    total = 0

    for expense in expenses:
        total += expense['amount']

    return float(total)

def get_all_categories() -> list:
    """
    Creates a list of all the expense categories.

    Returns:
        categories (list): A list of all the different expense categories.
    """
    categories = []

    for expense in expenses:
        if not expense['category'] in categories:
            categories.append(expense['category'])

    return categories

def get_category_total(category: str) -> float:
    """
    Totals the amount of a given category.

    Args:
        category (str): The name of the category.
    Returns:
        total (float): The total amount in the given category
    """
    total = 0

    for expense in expenses:
        if expense['category'] == category:
            total += expense['amount']

    return float(total)

def all_category_totals() -> list:
    """
    Gets the total sum of each category in the expenses database.

    Returns:
        category_totals_data (list): A list of dictionaries, each holding a
        category and its total sum.
    """
    category_totals_data = []

    for category in get_all_categories():
        total = get_category_total(category)
        category_totals_data.append({"category": category, "total": total})

    return category_totals_data

def biggest_expense() -> list:
    """
    Finds the biggest expense.

    Returns:
        (list): A list holding a dictionary of the biggest expense,
        or an empty list if there are no expenses.
    """
    big_expense = None

    for expense in expenses:
        if big_expense is None or expense['amount'] > big_expense['amount']:
            big_expense = expense

    return [big_expense] if big_expense else []

def show_summary() -> None:
    """
    Produces a summary of the expenses.
    It shows the total spent, the total for each category, and the biggest single expense.

    Returns:
        None.
    """

    # Overview Message
    print()
    print(menu_heading("Summary"))
    print("– The total spent")
    print("– The total for each category")
    print("– The biggest single expense\n")

    # Total Spent
    print(f"The total spent is: £{get_total():.2f}\n")

    # Total for each Category
    print("The total for each category:")
    print(make_table(all_category_totals()))

    # Biggest Single Expense
    print("\nThe biggest single expense is:")
    print(make_table(biggest_expense()))
    print()

# -------------------------------
# Make Table Function
# -------------------------------
def make_table(data: list) -> str:
    """
    Creates a table from the argument passed in.
    The argument must be a list of dictionaries.

    Returns:
        table (str): A table from the data passed in.
    """
    table = tabulate(data, headers="keys", tablefmt="psql", showindex="always")
    return table

# -------------------------------
# Menu Functions
# -------------------------------
def title(title_copy: str) -> str:
    """
    Creates a title from the argument.

    Returns:
        (fString) example:
            title("expense tracker"):
                ==============================
                EXPENSE TRACKER
                ==============================
    """
    l = "="*30
    the_title = title_copy.strip().upper()
    return f"{l}\n{the_title}\n{l}\n"

def menu_heading(copy: str) -> str:
    """
    Creates the menu heading from the argument.

    Returns:
        (fString) example:
            menu_heading("menu"):
                MENU
                ------------------------------
    """
    l = "-"*30
    the_heading = copy.strip().upper()
    return f"{the_heading}\n{l}"


# -------------------------------
# Get Answer Function
# -------------------------------
def get_answer() -> int:
    """
    Asks the user for an answer.

    Returns:
        answer (int): A number between 1 - 4.
    Raises:
        ValueError: If the value entered isn't a number.
        ValueError: If the value entered is more than 4 or less than 1.
    """
    while True:
        try:
            answer = int(input("Enter a number: "))
            if answer > 4 or answer < 1:
                print("Your answer must be within the number range.\n")
            else:
                return answer
        except ValueError:
            print("Please enter a correct value.\n")

def user_request(answer: int) -> None:
    """
    Runs the program depending on the output from the user.

    Args:
        answer (int): The number returned by get_answer().
    Returns:
        None. Depending on the answer:
        1 = add_expense(get_expense()): Gets the user to add an expense.
        2 = show_expenses(): Views all the expenses.
        3 = show_summary(): Shows a summary breakdown.
        4 = sys.exit(): Prints a goodbye message and quits the program.
    """

    # 1 – Add an Expense.
    if answer == 1:
        print()
        print(add_expense(get_expense()))
        print()

    # 2 – View All Expenses
    elif answer == 2:
        print()
        show_expenses()
        print()

    # 3 – Show Summary
    elif answer == 3:
        show_summary()

    # 4 – Exit
    elif answer == 4:
        print("Goodbye!")
        sys.exit()


if __name__ == "__main__":
    main()
