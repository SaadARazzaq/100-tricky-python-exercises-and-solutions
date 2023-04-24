
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 88 - Dictionaries
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct code in order to update the value associated with key 4 to "Cardano".
"""
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}


print(crypto[4])
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.update({4:'Cardano'})  #  You can also use syntax ' crypto[4] = "Cardano" '

print(crypto[4])