
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 99 - Dictionaries
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct method on line 10 in order to get a list of all the keys in the dictionary.
"""
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

keys = 

print(list(keys))
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

keys = crypto.keys()  # You can also use  'keys = crypto'

print(list(keys))