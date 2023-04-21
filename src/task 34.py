
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 34 - Numbers & Booleans
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct logical operator in between the two expressions on line 8 in order for the final result to be True.
"""
result = (min(pow(2, abs(3)), 9) == 3 ** 2 - 1)  (66 % 20 + 2 > 2 ** 3)

print(result) #should return True
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

result = (min(pow(2, abs(3)), 9) == 3 ** 2 - 1) or (66 % 20 + 2 > 2 ** 3)  # You can also use '|' instead of 'or'

print(result) #should return True