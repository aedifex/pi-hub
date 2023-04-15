
from data_model import user_name
from data_model import menu_items
from data_model import food_menu
from data_model import order_cart
from common import print_restaurant_menu
from common import get_string
from common import print_message
from common import get_cmd_selection
from common import get_quantity
from common import press_enter_to_continue
from common import get_user_name

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
    print(quantity)
    # Check if item exists in cart, if so, increment value
    # if not, create new cart entry
    if food_item in order_cart:
        order_cart[food_item] += quantity
    else:
        order_cart[food_item] = quantity


def display_shopping_cart():
    """
        display_shoppihg_cart function is the callback when the user selects the command display shopping cart

        Parameters:
            None
        
        Returns:
            None

    """
    # The format string used for printing the header and the menu item
    format_str = "        | {:<11}| {:<9}| {:<7}| {:<18} |"
    print("        "+"-"*55)
    # The header for the menu
    print (format_str.format('Item','Quantity','Price','Preparation Time'))
    print("        "+"-"*55)

    for m_key, quantity in order_cart.items():
        m_item         = menu_items[m_key-1]['Name']
        m_price        = f"${menu_items[m_key-1]['Price']*quantity:4}"
        m_prep_time    = f"{menu_items[m_key-1]['PrepTime']*quantity:4} mins"
        print (format_str.format(m_item, quantity, m_price, m_prep_time))
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

# The function name is check_out()
# This must calculate the discout, total price etc., and print the Bill
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
    recipt = {"Sandwich": {"Total_Before_Discount" : 0, "Total_After_Discount" : 0, "Discount": 0}, 
              "Salad": {"Total_Before_Discount" : 0, "Total_After_Discount" : 0, "Discount": 0},
              "Soup": {"Total_Before_Discount" : 0, "Total_After_Discount" : 0, "Discount": 0},
              "Coffee/Tea": {"Total_Before_Discount" : 0, "Total_After_Discount" : 0, "Discount": 0}}

    print(order_cart) # {1: 1, 3: 3}
    for key in order_cart.keys():
        print(food_menu[key]["Name"])
        # Keys our abstraction food_menu[key]["Name"]
        # To another datastructure we use to tabulate total

        # Calculate price before discount
        recipt[food_menu[key]["Name"]]["Total_Before_Discount"] = order_cart[key] * food_menu[key]["Price"]

        # !!!Calculate discount!!!
        if order_cart[key] > food_menu[key]["discountquantity"]:
            print(f'Discount for { food_menu[key]["Name"][0].lower() + food_menu[key]["Name"][1:] } is: {food_menu[key]["Discount"]}%')
           
            # Calculate price after discount
            discount = food_menu[key]["Discount"] / 100
            print(f'Discount: {discount}')

        
        recipt[food_menu[key]["Name"]]["Total_After_Discount"] = recipt[food_menu[key]["Name"]]["Total_Before_Discount"] - (recipt[food_menu[key]["Name"]]["Total_Before_Discount"] * discount) 

    print(recipt["Sandwich"]["Total_Before_Discount"])
    print(recipt)

    final_recipt = format_recipt(recipt)

def format_recipt(recipt):
    """
        check_out function computes the time and bill for the order

        Paramters: None

        Returns: None
    """
    name = get_user_name()
    # Calculate the width of each column based on the longest item name and price
    # item_width = max([len(key) for key in recipt.keys()]) + 2  # Add 2 for padding
    #qty_width = 4  # Always use 4 characters for the quantity
    # price_width = len("{:.2f}".format(max(recipt.values()))) + 2  # Add 2 for padding
    formatted_recipt = f"""
    {'*'*50}
    {name}, thanks for your order
    {'*'*50}
    """
    return formatted_recipt
