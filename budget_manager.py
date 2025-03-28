from urllib.parse import parse_qs
from budget import *

# Global variables to keep track of the transactions and balance
budget_data = {'balance': 0.0, 'transactions': {'incomes': [], 'expenses': []}}

def application(environ, start_response):
    global budget_data

    # Create the response body based on the action
    method = environ['REQUEST_METHOD']
    query_string = environ.get('QUERY_STRING', '')
    form_data = parse_qs(query_string)

    # Default form for selecting an action
    if method == 'GET':
        return get_form(start_response)

    # Handle POST actions
    if method == 'POST':
        try:
            # Parse the form data (we need to read the body)
            content_length = int(environ.get('CONTENT_LENGTH', 0))
            if content_length:
                raw_input = environ['wsgi.input'].read(content_length)
                form_data = parse_qs(raw_input.decode('utf-8'))
            else:
                form_data = {}
        except Exception as e:
            form_data = {}

        action = form_data.get('action', [''])[0]

        if action == 'add_income':
            return get_add_income_form(start_response)

        elif action == 'add_expense':
            return get_add_expense_form(start_response)

        elif action == 'show_balance':
            return show_balance_page(budget_data, start_response)

        elif action == 'show_history':
            return show_history_page(budget_data, start_response)

        # Handle adding income
        if 'income' in form_data:
            new_budget_data, response = add_income(form_data,budget_data,start_response)
            if new_budget_data:
                budget_data=new_budget_data.copy()
            return response

        # Handle adding expense
        if 'expense' in form_data:
            new_budget_data, response = add_expense(form_data, budget_data, start_response)
            if new_budget_data:
                budget_data = new_budget_data.copy()
            return response

    # Default to showing the main form
    return get_form(start_response)
