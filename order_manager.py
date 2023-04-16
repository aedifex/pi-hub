
from data_model import menu_items
from data_model import order_cart
from common import print_restaurant_menu
from common import get_string
from common import print_message
from common import get_cmd_selection
from common import get_quantity
from common import press_enter_to_continue

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
    format_str = "        | {:<11}| {:<9}| {:<7}| {:<18} |"
    print("        "+"-"*55)
    # The header for the menu
    print (format_str.format('Key', 'Item','Quantity','Price','Preparation Time'))
    print("        "+"-"*55)

    for m_key, quantity in order_cart.items():
        m_item         = menu_items[m_key-1]['Name']
        m_price        = f"${menu_items[m_key-1]['Price']*quantity:4}"
        m_prep_time    = f"{menu_items[m_key-1]['PrepTime']*quantity:4} mins"
        print (format_str.format(m_key, m_item, quantity, m_price, m_prep_time))
    print("        "+"-"*55)
    print_message("All Discounts will be applied at the checkout.")
    press_enter_to_continue()
        
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

        delete_item_shopping_cart first calls the shopping cart to give the user a look of the cart
        and then asks the user to select the food item.
        Finally it will remove the item from the cart.

        Parameters:
            None
        
        Returns:
            None

    """
    print("\n            ***You are REMOVING item from your CART!***")
    display_shopping_cart()
    print("\n")
    #r_item = get_cmd_selection(4)
    r_item = int(input("Enter the KEY of the item you want to REMOVE from your shopping cart: "))
    order_cart.pop(r_item)
    print("\nThis is the updated Shopping Cart")
    display_shopping_cart()


def check_out():
    """
        check_out function computes the time and bill for the order

        Paramters: None

        Returns: None
    """
    pass