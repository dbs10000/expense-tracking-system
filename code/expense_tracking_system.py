# ===============================================================
# Expense Tracking System
# ---------------------------------
# A simple expense tracking system. 
# 
# ===============================================================



# ---------------------------------
# Database Simulation
# ---------------------------------
expenses = []



# ---------------------------------
# Expense Function
# ---------------------------------
def add_expense(amount: int, category: str, description: str) -> dict:
    """
    Creates an expense and adds it to the list of expenses.
    
    Args:
        amount (int): The price of the expense. Gets converted into a float.
        category (str): The category of the expense.
        description (str): A brief description of the expense.

    Returns:
        expense (dict): The expense as a dictionary if the expense is valid.

    Raises:
        ValueError: If the amount is less than or equal to 0.
    """

    # Validates the amount is greater than 0 
    if amount <= 0:
        raise ValueError("The amount needs to be greater than 0")
        

    float_amount = float(amount)
    # Creates a dictionary of for the expense data
    expense = {
        "amount" : float_amount,
        "category" : category,
        "description" : description
    }

    # Adds the new expense to the expenses list.
    expenses.append(expense)

    # Returns the expense dictionary
    return expense



# ---------------------------------
# Calculate Total Function
# ---------------------------------
def calculate_total_expenses() -> int:
    """
    Calculates the total amount of expenses

    Returns:
        total (int): The total sum of expenses
    """

    # Loops through the expenses dict and totals the amount.
    total = 0
    for expense in expenses:
        total += expense['amount']

    # Returns the total
    return total
    


# ---------------------------------
# Calculate Total By Category Function
# ---------------------------------
def calculate_total_by_category(category: str) -> int:
    """
    Calculates the total amount of expenses based on a category.

    Args:
        category (str): The expenses category.
    
    Returns:
        category_total (int): The total amount within the category.
    """

    # Loops through the expenses dict and filters out the selected category.
    # Creates a total sum of the expenses within that specific category.
    category_total = 0
    for expense in expenses:
        if expense["category"] == category:
            category_total += expense["amount"]
    return category_total



# ---------------------------------
# Show Expenses Function
# ---------------------------------
# This function clearly displays all the stored expenses
def show_expenses() -> str:
    """
    Shows all the expenses in a neat and tidy way.
    """
    print("-" * 30)
    print("ALL STORED EXPENSES")
    for index, expense in enumerate(expenses, start=1):
        print("-" * 30)
        print("Expense Index: ", index)
        print("Category: ", expense['category'])
        print("Description: ", expense['description'])
        print(f"Amount: £{expense['amount']}")
    print("-" * 30)
    print(f"TOTAL EXPENSES: £{calculate_total_expenses()}")



# ---------------------------------
# TESTING
# ---------------------------------

# Adding Expenses
# ---------------------------------
add_expense(39.5, "food", "Shopping for the week")
add_expense(8, "transport", "The tube and bus")
add_expense(3.62, "food", "A chocolate bar from pret")
# add_expense(-39.42, "error", "error")


# Printing result
# ---------------------------------
# Variable to hold food total
food_total = calculate_total_by_category("food")
transport_total = calculate_total_by_category("transport")

print("-" * 30)
print("Category".upper())
print("-" * 30)
print(f"Food Total: £{food_total}")
print(f"Transport Total: £{transport_total}")
print("-" * 30)
print()
show_expenses()