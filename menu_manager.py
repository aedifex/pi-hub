"""
Module: data-model.py
Authors: chris, clarence, pals

This module defines the basic data model for the Restaurant Ordering Application.

"""


from common import print_message
from common import get_string
from common import get_cmd_selection
from common import print_restaurant_menu
from common import press_enter_to_continue

from data_model import food_menu
from data_model import user_name


from order_manager import select_food
from order_manager import display_shopping_cart
from order_manager import clear_shopping_cart
from order_manager import check_out

"""
cmd_items is a list and contains the list of command menus
that the Restaurant Application provides to the user.
"""
cmd_items = [
            "1 - Display Food Menu",
            "2 - Display Shopping Cart",
            "3 - Clear Shopping Cart",
            "4 - Select Food",
            "5 - Check Out",
            "6 - Exit without ordering"
    ]


def print_restaurant_banner():
    """
    print_restaurant_banner function prints restaurant menu

    print_restaurant_banner is an internal function and provides information about 
    the restaurant menu and what the user can do with that.

    Parameters:
        None

    Returns:
        None
    """

    help_str =  '''
        **************************************************************
        *           Welcome to the Restaurant Ordering System        *
        *    This Ordering system provides the menu for Restaurant   *
        *                       Food Ordering.                       *
        * Users can order Food items, as many items they want        * 
        *    The menus system calculates the total time taken        *
        *           for the order and prints the receipt             *
        **************************************************************
    '''
    # Print the above help message. Also use the flush=True parameter to send the complete
    # help message to the screen before asking the user for input.
    # If we don't flush, the input comes first sometimes.
    print(help_str, flush=True)

def print_cmd_items(cmd_items):
    """
    print_cmd_items method prints the command menu options

    Parameters:
        None

    Returns:
        None

    """
    for cmd_item in cmd_items:
        print_message(cmd_item)


def main_loop(cmd_items):
    """
    main_loop is the main loop of the Restaurant Ordering System


    main_loop function runs forever until user exits
        1. prints the menu, 
        2. calls the _get_input() to get a selection from the user
        3. call the overridden process_command()

    Parameters:
        None

    Returns:
        None
    """
    # Print the banner once
    print_restaurant_banner()
    user_name = get_string("Please enter your name", 4)
    while True:
        # First print the menu for this version
        print_message("**************************************************************")
        print_message("*"*22+" SELECT AN OPTION "+ "*"*22)
        print_cmd_items(cmd_items) 
        # Get user Selection
        selection = get_cmd_selection(len(cmd_items))
        # Process the command by calling process_command
        result = process_command(selection)
        if result.lower() == "exit":
            # Before we exit, we save our employee to the 
            # database. We should normally call a method in the database class
            # however, for this project we just overwrite the element in the list.
            print_message("Thank you for using the Restaurant Ordering Application.")
            print_message("Hope you enjoyed your meal.")
            return

def process_command(selection):
    """
    process_command is the input processing function
    *** NOTE: This function is overridden in the V2 and V3 versions ***

    process_command function returns "exit" to indicate command processing is done.

    Parameters:
        selection (int): The user selection. 

    Returns:
        (str) : "exit" to indicate exit the loop. Otherwise, empty string.
    """
   
    if selection == 1:
        print_restaurant_menu()
        press_enter_to_continue()
    elif selection == 2:
        display_shopping_cart()
    elif selection == 3:
        clear_shopping_cart()
    elif selection == 4:
        select_food()
    elif selection == 5:
        check_out()
    elif selection == 6:
        return "Exit"

    return ""