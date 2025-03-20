budget_data = { "balance": 0,
"transactions": {
"income": [], ### (300, "Drugs"), (400, "Sex")
"expense": [] ### (500, "Rock N' Roll)
}
}

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

# Budget Manager
# 1. Add Income
# 2. Add Expense
# 3. Show Balance
# 4. Show Transaction History
# 5. Exit

print("Welcome to the Budget Manager\n\n")

user_input=get_valid_option(["Add Income",
                           "Add Expense",
                           "Show Balance",
                           "Show Transaction History",
                           "Exit"])

while user_input != 5:
    match (user_input):
        case 1:
            sum=get_valid_float("Please insert the sum to add")
            comment=get_valid_string("Please insert a comment for the income")
            #
            ### add_income(budget_data, sum, comment) ### Don't forget to calculate balance
        case 2:
            sum = get_valid_float("Please insert the sum to reduce")
            comment = get_valid_string("Please insert a comment for the expense")
            #
            ### add_expense(budget_data, sum, comment) ### Don't forget to calculate balance
        case 3:
            pass
            ### show balance
            #
            ### show_balance(budget_data)
        case 4:
            pass
            ### Show transaction history
            #
            ### show_transaction_history(budget_data)
        case _:
            print("How did you get here????")

    user_input = get_valid_option(["Add Income",
                                 "Add Expense",
                                 "Show Balance",
                                 "Show Transaction History",
                                 "Exit"])

print("\n\nSee you again soon!!!\n\n")
