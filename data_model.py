"""
Module: data-model.py
Authors: chris, clarence, pals

This module defines the basic data model for the Restaurant Ordering Application.

1. Menu Items data model
   This is a python list with each element modeled as menu item.

2. Menu Item
   A Menu Item is a dictionary with the following fields, and defines an orderable food item along
   with its properties
   Name:  Food Item Name like sandwich
   Price: The price of the item in Dollars
   Discout: The maximum discount percentage when this food item is ordered and when it satisfies certain conditions, per item of the order.
   PrepTime: Time taken in minutes to prepare and serve the food item
   DiscountStr: User readable string that defines the terms the must be met for the discount to be applicable
   discountpair: The associated food item. Note: This is an internal model element and used for compute
   discountquantity: The number of items of this type that must be ordered for the getting the discount.

3. Food Menu
   Food Menu is a dictionary that contains the each menu item along with the key
   The key is an unique integer that is used for selection and identifying the food item

4. Order Cart
   The order Cart is a dictionary and contains the order placed by a single user.
   The key is the Menu Item Key and the value is the quantity.

5. User Name
   The Name of the User for printing the Bill


"""
# Menu items list as defined above
menu_items = [
    {
        "Name": "Sandwich",
        "Price": 10,
        "Discount": 10,
        "PrepTime": 10,
        "DiscountString": "if 5 or more are ordered",
        "discountpair": ["Sandwich"],
        "discountquantity": 5
    },
    {
        "Name": "Salad",
        "Price": 8,
        "Discount": 10,
        "PrepTime": 8,
        "DiscountString": "if ordered with a Soup",
        "discountpair": ["Soup"],
        "discountquantity": 0
    },
    {
        "Name": "Soup",
        "Price": 6,
        "Discount": 20,
        "PrepTime": 15,
        "DiscountString": "if ordered with sandwich and salad",
        "discountpair": ["Sandwich", "Salad"],
        "discountquantity": 0
    },
    {
        "Name": "Coffee/Tea",
        "Price": 5,
        "Discount": 0,
        "PrepTime": 5,
        "DiscountString": "No Discount.",
        "discountpair": [],
        "discountquantity": 0
    }
]

# Food Menu
food_menu = {
    1: menu_items[0],
    2: menu_items[1],
    3: menu_items[2],
    4: menu_items[3]
}

# Order Cart
order_cart = {

}

# User Name
user_name = ""