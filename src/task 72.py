
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 72 - Tuples
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct method on line 10 in order to find out the last element of my_tup in alphabetical order.
"""
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

last = 

print(last) #should return Slovenia
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

last = sorted(my_tup)[-1]  # You can also use 'last = max(my_tup)' instead

print(last) #should return Slovenia