
from data_model import menu_items
from data_model import order_cart
from data_model import food_menu
from common import print_restaurant_menu
from common import get_string
from common import print_message
from common import get_cmd_selection
from common import get_quantity
from common import press_enter_to_continue
from common import get_order_keys
import sys
import datetime

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
    print_message("\n        Shopping Cart")
    # The format string used for printing the header and the menu item
    format_str = "        | {:<4}| {:<12}| {:<10}| {:<8}| {:<10}| {:<18} |"
    print("        "+"-"*75)
    # The header for the menu
    print (format_str.format('Key', 'Item','Quantity', 'Price','Subtotal','Preparation Time'))
    print("        "+"-"*75)

    for m_key, quantity in order_cart.items():
        m_item         = menu_items[m_key-1]['Name']
        m_price        = "{:>8}".format("${:.2f}".format(menu_items[m_key-1]['Price']))
        m_subtotal     = "{:>8}".format("${:.2f}".format(menu_items[m_key-1]['Price']*quantity))
        m_prep_time    = f"{menu_items[m_key-1]['PrepTime']*quantity:4} mins"
        print (format_str.format(m_key, m_item, quantity, m_price, m_subtotal, m_prep_time))
    print("        "+"-"*75)
    print_message("      *** All Discounts will be applied at the checkout ***.\n")
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

        delete_item_shopping_cart first validates if the dictionary is empty or not. If not empty, then it calls the delete_item_shopping_cart function to give the user a look of the cart
        and then asks the user to select the food item to remove from the shopping cart.
        This function also validates for any invalid entries like negative entry, or quantity entry greater than the actual recorded quantity. 
        If it passes the validation, it will subtract the quantity the user entered from the original quantity. 
        If the user-entered quantity is equal to the recorded quantity, it removes the item from the cart.  
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
        if r_item in order_cart:
            try:
                qty = int(input("\n            Enter the quantity to remove: "))
                orig_qty = order_cart.get(r_item, 0)
                if qty < 0 or qty > orig_qty:
                    print("\n            *** Quantity is incorrect. Try again. ***")
                elif qty == orig_qty:
                    del order_cart[r_item]
                    print("            *** Below is the UPDATED Shopping Cart. ***")
                else:
                    order_cart[r_item] = orig_qty - qty
                    print(f"\n            *** Quantity {qty} has been removed for item {r_item}. ***")
                    print("            *** Below is the UPDATED Shopping Cart. ***")
                display_shopping_cart()
            except ValueError:
                print("            *** Invalid quantity entered. Please try again. ***")
        else:
            print(f"\n            *** {r_item} not found in the shopping cart. ***")

        press_enter_to_continue()




def check_out():
    """
        check_out function computes the time and bill for the order

        Paramters: None

        Returns: None
    """
    calculate_total()

def calculate_total():
    """
        calculate_total calculates total cost and stores data in recipt object

        Paramters: None

        Returns: A calculated recipt object.
    """
    # dicts of dicts
    # recipt = {key: menu_items["Name"] for key in menu_items : {"Total" : 0, "Discount": 0}}
    recipt = {"Sandwich": {"Total_Before_Discount" : 0, "Total_After_Discount" : 0, "Discount": 0, "Qty": 0},
              "Salad": {"Total_Before_Discount" : 0, "Total_After_Discount" : 0, "Discount": 0, "Qty": 0},
              "Soup": {"Total_Before_Discount" : 0, "Total_After_Discount" : 0, "Discount": 0, "Qty": 0},
              "Coffee/Tea": {"Total_Before_Discount" : 0, "Total_After_Discount" : 0, "Discount": 0, "Qty": 0}}

    for key in order_cart.keys():
        # Keys our abstraction food_menu[key]["Name"]
        # To another datastructure we use to tabulate total

        # Calculate price before discount
        recipt[food_menu[key]["Name"]]["Total_Before_Discount"] = order_cart[key] * food_menu[key]["Price"]
        recipt[food_menu[key]["Name"]]["Qty"] = order_cart[key]

        # !!!Calculate discount!!!
        if order_cart[key] > food_menu[key]["discountquantity"]:
            # print(f'Discount for { food_menu[key]["Name"][0].lower() + food_menu[key]["Name"][1:] } is: {food_menu[key]["Discount"]}%')
            # Calculate price after discount
            discount = food_menu[key]["Discount"] / 100
            # print(f'Discount: {discount}')
            recipt[food_menu[key]["Name"]]["Total_After_Discount"] = recipt[food_menu[key]["Name"]]["Total_Before_Discount"] - (recipt[food_menu[key]["Name"]]["Total_Before_Discount"] * discount)
        # Calc discount for different permuttations
    final_recipt = format_recipt(recipt)

    print(final_recipt)
    sys.exit(0)

def format_recipt(recipt):
    """
        format_recipt accepts a recipt object and formats the values using f-strings and format specifiers

        Paramters: a recipt object (a dictionary of dictionaries)

        Returns: None
    """
    # Get the current date
    now = datetime.datetime.now()

    # Format the date as a string
    date_str = now.strftime("%m/%d/%y")
    # subtotal = sum(qty * price for name, qty, price in items)
    # total = subtotal * (1 + tax)
    # We "create" a recipt with processed values
    # user name isn't displaying??
    # Calculate total
    total = 0
    # Calculate tax
    tax = 0.0725

    # Calculate order time
    prep_time = 0
    # we take the greatest time
    for m_key, quantity in order_cart.items():
        if  float(f"{menu_items[m_key-1]['PrepTime']*quantity:4}") > prep_time:
            prep_time = float(f"{menu_items[m_key-1]['PrepTime']*quantity:4}")

    formatted_recipt = f"""{' ' * 8}{'*' * 62}
{' ' * 8}{"Chris"}, thanks for your order\n
{' ' * 8}{'Items':<20}{'Qty':<10}Price
{' ' * 8}{'-' * 35}"""

    for item in recipt.keys():
       if recipt[item]["Total_After_Discount"] > 0:
            total += recipt[item]["Total_After_Discount"]
            # Apply tax
            total -= total * tax
            formatted_recipt += f"""
{" " * 8}{item:<20}{recipt[item]["Qty"]:<10}{recipt[item]["Total_After_Discount"]:>5.2f}\n"""

    formatted_recipt += f"""
{' ' * 8}{'-' * 35}
{' ' * 8}{'Tax':<8} {tax:>5.2f}%
{' ' * 8}{'Total':<8}${total:>5.2f}\n
{' ' * 8}{date_str+",":<8} your order will be ready in {prep_time} mins
{' ' * 8}{'*' * 62}
"""
    return formatted_recipt