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
        amount (int): The price of the expense.
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

    # Creates a dictionary of for the expense data
    expense = {
        "amount" : amount,
        "category" : category,
        "description" : description
    }

    # Adds the new expense to the expenses list.
    expenses.append(expense)

    # Returns the expense dictionary
    return expense