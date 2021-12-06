multi_line = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

"""
global order_amount
order_amount = 0

# def get_user_order():
  
print(multi_line)
order = input("> ")

while order != "quit":
  order_amount+=1
  print(f"** {order_amount} order of {order} have been added to your meal **")
  order = input("> ")
if order == "quit":
  print("Thank you for visiting.")
  






# get_user_order()
#Appetizers
# ----------
# Buffalo Wingz
# SnickerDoodles
# Spring Rolls

# Entrees
# -------
# Vegan Smoked Salmon
# All hail seitan Steak
# Meatless Tornado
# Rabbit Food

# Desserts
# --------
# Ice Cream
# Cake
# Pie

# Drinks
# ------
# Coffee
# Tea
# Consensual Unicorn Tears
