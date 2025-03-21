from budget import *

budget_data = { "balance": 0,
"transactions": {
"income": [], ### (300, "Drugs"), (400, "Sex")
"expense": [] ### (500, "Rock N' Roll)
}
}


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
            pass
            #
            ### add_income(budget_data)
        case 2:
            pass
            #
            ### add_expense(budget_data)
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
