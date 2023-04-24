
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 73 - Tuples
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct method on line 10 in order to find out the number of occurrences of Estonia in my_tup.
"""
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Estonia", "Romania", "Hungary", "Slovenia")

number = my_tup.

print(number)
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Estonia", "Romania", "Hungary", "Slovenia")

number = my_tup.count("Estonia")

print(number)