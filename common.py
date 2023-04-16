"""
Module: common.py
Authors: chris, clarence, pals

This module keeps all the common and utility functions.

"""

from data_model import food_menu
from data_model import user_name
from data_model import order_cart

def print_message(message):
    """
    print_string method prints a string formatted to output 

    Parameters:
        message (str): The message to be printed

    Returns:
        None

    """
    print(f"        {message}", flush=True)
        
def get_string(prompt, minlen):
    """
    get_string method get a string input from the user.

    get_string method is an internal method and prompts the user with
    the given message and asks the user to enter a value.
    It validates the input provided by the user to the minimum length
    required. 

    Parameters:
        prompt (str): The prompt message that is provided to the user
        minlen (int): The minimum length the input should be provided.

    Returns:
        value_str (str) : The string value entered by the user.

    """
    value_str = ""
    while True:
        value_str = input(f"            {prompt} : ")
        if len(value_str) >= minlen:
            break
        print_message(f"Please enter a value with length >= {minlen}!")  
    return(value_str)

def get_cmd_selection(num_items):
    """
    get_cmd_selection method gets the user command menu selection

    get_cmd_selection method is an internal method and asks the user to
    select a command menu option. If the user selects an option that is 
    not within the available options it prints an error message
    and asks the user to try again.

    Parameters:
        num_items (int): number of items in the menu.

    Returns:
        selection (int) : The selected menu item

    """
    selection = -1
    prompt = f"Please select a menu option [1,{num_items}]"
    while True:
        selection_str = get_string(prompt, 1)
        try:
            selection = int(selection_str)
            if selection >= 1 and selection <= num_items:
                return selection
            print_message(f"Please select a valid menu item between [1, {num_items}].")
        except ValueError:
            print_message(f"The selection: '{selection_str}' is invalid integer, please enter an integer between [1, {num_items}].")

def get_order_keys():
    """
    get_order_keys method gets the user command menu selection

    get_order_keys method is an internal method and asks the user to
    select a key as a selection or option within the order_cart
    and asks the user to try again.

    Parameters:
        key_order_item (int): list of keys within the order cart

    Returns:
        selection (int) : The selected menu item

    """
    selection = -1
    key_order_item = list(order_cart.keys())
    prompt = f"Select item to remove. Options {key_order_item}"
    while True:
        selection_str = get_string(prompt, 1)
        try:
            selection = int(selection_str)
            if selection in order_cart:
                return selection
            print_message(f"Please select a valid item. Options {key_order_item}:")
        except ValueError:
            print_message(f"The selection: '{selection_str}' is invalid option. Options: {key_order_item}.")

def get_quantity(prompt):
    """
    get_quantity method gets quantity of the selected food item

    Parameters:
        None

    Returns:
        quantity (int) : The quantity of the food item

    """
    quantity = -1
    while True:
        quantity_str = get_string(prompt, 1)
        try:
            quantity = int(quantity_str)
            return quantity
        except ValueError:
            print_message(f"The selection: '{quantity_str}' is invalid integer, please enter an integer.")

def print_restaurant_menu():
    """
    print_restaurant_menu function prints the menu for user selection

        print_restaurant_menu function is used for printing and displaying the
        food menu items to the user.
        The function iterates over the food_menu dictionary and prints the items
        and the key in a user friently manner
        The user selects the menu item by providing the key integer

        Parameters:
            None
        Returns:
            None
    """
    # The format string used for printing the header and the menu item
    format_str = "        | {:<2}| {:<11}| {:<7}| {:<39}| {:<16} |"
    print("        "+"-"*87)
    # The header for the menu
    print (format_str.format('No','Item','Price','Discount','Preparation Time'))
    print("        "+"-"*87)
    for m_key, menu_item in food_menu.items():
        m_item         = menu_item['Name']
        m_price        = f"${menu_item['Price']:2}"
        m_discount_str = f"{menu_item['Discount']:-2}% {menu_item['DiscountString']}"
        m_prep_time    = f"{menu_item['PrepTime']:2} mins"
        print (format_str.format(m_key, m_item, m_price, m_discount_str, m_prep_time))
    print("        "+"-"*87)

def get_user_name():
    """
        get_user_name function returns the name of user ordering food

        Parameters:
            None
        
        Returns:
            (str): The username
    """
    # This function returns the username stored in the data model
    return user_name

def press_enter_to_continue():
    """
        press_any_key_to_continue function pauses for user input

        Parameters:
            None
        Returns:
            None
    """
    _ = input("        Press Enter to continue .....")
    return