
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 89 - Dictionaries
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct code in order to add a new key-value pair to the dictionary: 6: "Monero"
"""
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

print(crypto[6])
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto[6] = "Monero" # You can also use crypto.update({6:"Monero"})

print(crypto[6])