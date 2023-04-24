
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 100 - Dictionaries
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct method in order to return and remove an arbitrary key-value pair from the dictionary.
"""
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}


print(len(crypto))
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.popitem()

print(len(crypto))