
from data_model import menu_items
from data_model import order_cart
from common import print_restaurant_menu
from common import get_string
from common import print_message
from common import get_cmd_selection
from common import get_quantity
from common import press_enter_to_continue
from common import get_order_keys

def select_food():
    """
        select_food function is the callback when the user selects the command select food.

        select_food first calls the display menu to give the user a look of the menu
        and then asks the user to select the food item.
        Then it will also ask the user to input the quantity
        Finally it will add the item to the cart.

        Parameters:
            None
        
        Returns:
            None

    """
    print_restaurant_menu()
    food_item = get_cmd_selection(4)
    quantity  = get_quantity("Please enter the quantity")
    if food_item in order_cart:
        order_cart[food_item] += quantity
    else:
        order_cart[food_item] = quantity

def display_shopping_cart():
    """
        display_shopping_cart function is the callback when the user selects the command display shopping cart

        Parameters:
            None
        
        Returns:
            None

    """
    # The format string used for printing the header and the menu item
    format_str = "        | {:<4}| {:<11}| {:<9}| {:<7}| {:<18} |"
    print("        "+"-"*61)
    # The header for the menu
    print (format_str.format('Key', 'Item','Quantity','Price','Preparation Time'))
    print("        "+"-"*61)

    for m_key, quantity in order_cart.items():
        m_item         = menu_items[m_key-1]['Name']
        m_price        = f"${menu_items[m_key-1]['Price']*quantity:4}"
        m_prep_time    = f"{menu_items[m_key-1]['PrepTime']*quantity:4} mins"
        print (format_str.format(m_key, m_item, quantity, m_price, m_prep_time))
    print("        "+"-"*61)
    print_message("All Discounts will be applied at the checkout.")
    #press_enter_to_continue()

def clear_shopping_cart():
    """
        clear_shopping_cart function empties the shopping cart

        Parameters: None

        Returns: None
    """
    yes_no = get_string("Are you sure you want to discard all items in the cart <y/N>", 1)
    if yes_no.upper() == 'YES' or yes_no.upper()[0] == 'Y':
        print_message("Clearing the cart ...")
        #order_cart = {}
        order_cart.clear()
    else:
        print_message("Cart is not cleared, please continue.")
    return

def delete_item_shopping_cart():
    """
        delete_item_shopping_cart function removes an item in the shopping cart

        delete_item_shopping_cart first validates if the dictionary is empty or not. If not empty, then it calls the shopping cart to give the user a look of the cart
        and then asks the user to select the food item to remove from the shopping cart
        Finally it will remove the item from the cart.
        If the dictionary order_cart is empty, then display a message.

        Parameters:
            None
        
        Returns:
            None

    """
    if len(order_cart) > 0:
        print("\n            *** You are REMOVING item from your CART! ***")
        display_shopping_cart()
        print("\n")
        r_item = get_order_keys()
        order_cart.pop(r_item)
        print(f"            *** Item {r_item} is removed from the shopping cart. ***")
        print("            *** Below is the UPDATED Shopping Cart. ***")
        display_shopping_cart()
    else:
        print("\n        Shopping Cart is EMPTY! Nothing to remove.")
        print("\n        Please ADD items to your shopping cart.\n")
        press_enter_to_continue()


def check_out():
    """
        check_out function computes the time and bill for the order

        Paramters: None

        Returns: None
    """
    pass