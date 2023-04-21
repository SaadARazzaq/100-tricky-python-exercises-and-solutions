
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 35 - Numbers & Booleans
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct function on line 8 (for which the argument sits inside the parentheses) in order for the final result to be False.
"""
result = (150 % (10 ** 2 / 2))

print(result) #should return False
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

result = bool(150 % (10 ** 2 / 2))

print(result) #should return False