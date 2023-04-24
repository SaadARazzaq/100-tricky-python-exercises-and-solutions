
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 95 - Dictionaries
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct code on line 10 in order to get a list of tuples, where each tuple represents a key-value pair in the dictionary.
"""
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

result = 

print(list(result))
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

result = crypto.items()

print(list(result))