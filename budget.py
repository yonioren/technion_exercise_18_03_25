### Interactive functions ###
def get_valid_option(options, prompt):
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
            if prompt:
                prompt=prompt.strip()+": "
            value = float(input(prompt))

            if value > 0:
                return value
            else:
                print("Please enter a value greater than 0.\n")
        except ValueError:
            print("Invalid input, please enter a valid number.\n")


def get_valid_string(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        else:
            print("Invalid input, the string cannot be empty.\n")

#### Logic functions ####

#
## Add income to the budget.
## Allow multiple additions.
## Recalculate balance
## Return the budget after additions
#

# def add_income(budget_data:dict):
    # sum = get_valid_float("Please insert the sum to add")
    # comment = get_valid_string("Please insert a comment for the income")
    # ???
    # return new_budget_data

#
## Add expense to the budget.
## Allow multiple expenses.
## Recalculate balance.
## Return the budget after expenses.
#

# def add_expense(budget_data:dict):
    # sum = get_valid_float("Please insert the sum to reduce")
    # comment = get_valid_string("Please insert a comment for the expense")
    # ???
    # return new_budget_data

#
## Print the balance of the budget
## Do not return anything
#

# def show_balance(budget_data:dict):

#
## Print the transaction history of the budget
## Separate to incomes and expenses
#

# def show_transaction_history(budget_data:dict):