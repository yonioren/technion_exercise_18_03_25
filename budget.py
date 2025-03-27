### Interactive functions ###
def get_valid_option(options, prompt=None):
    while True:
        try:
            if prompt:
                print(prompt)

            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")

            # Get user input
            selection=int(input(f"Please select an option (1-{len(options)}): "))

            if 1 <= selection <= len(options):
                return selection
            else:
                print("Invalid selection, please choose a valid number from the list.\n")
        except ValueError:
            print("Invalid input, please enter a valid number.\n")


def get_valid_float(prompt):
    while True:
        try:
            if prompt and not prompt.strip()[-1] == ":":
                prompt=prompt.strip()+": "
            value = float(input(prompt))

            if value > 0:
                return value
            else:
                print("Please enter a value greater than 0.\n")
        except ValueError:
            print("Invalid input, please enter a valid number.\n")

def get_valid_string(prompt):
    if prompt and not prompt.strip()[-1] == ":":
        prompt = prompt.strip() + ": "

    while True:
        value = input(prompt).strip()

        if value:
            return value
        else:
            print("Invalid input, the string cannot be empty.\n")

def get_valid_y_n(prompt):
    if prompt:
        prompt=prompt.strip()+" (Y/n): "
    value = get_valid_string(prompt)

    while True:
        if value.lower() not in ['n','y']:
            value = get_valid_string("Y/n? ")
        else:
            break

    return value.lower() == 'y'

#### Logic functions ####

#
## Add income to the budget.
## Allow multiple additions.
## Recalculate balance
## Return the budget after additions
#

def add_income(budget_data:dict):
    while True:
        sum = get_valid_float("Please insert the sum of the income")
        comment = get_valid_string("Please insert a comment for the income")
        new_budget=budget_data.copy()
        new_budget["transactions"]["income"].append((sum,comment))
        new_budget["balance"]+=sum
        if not get_valid_y_n("Would you like to insert another income"):
            return new_budget

#
## Add expense to the budget.
## Allow multiple expenses.
## Recalculate balance.
## Return the budget after expenses.
#

def add_expense(budget_data:dict):
    while True:
        sum = get_valid_float("Please insert the sum of the expense")
        comment = get_valid_string("Please insert a comment for the expense")
        new_budget = budget_data.copy()
        new_budget["transactions"]["expense"].append((sum, comment))
        new_budget["balance"] -= sum
        if not get_valid_y_n("Would you like to insert another expense"):
            return new_budget

#
## Print the balance of the budget
## Do not return anything
#

def show_balance(budget_data:dict):
    print (f"The current budget is {budget_data['balance']}")

#
## Print the transaction history of the budget
## Separate to incomes and expenses
#

def show_transaction_history(budget_data:dict):
    for aspect in ["income", "expense"]:
        aspect_data = budget_data["transactions"][aspect]
        if len(aspect_data) > 0:
            print(aspect.upper())
            for transaction in aspect_data:
                print(f"\tAmount : {transaction[0]}\t\tComment : {transaction[1]}")
