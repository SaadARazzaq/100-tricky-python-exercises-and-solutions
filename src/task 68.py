
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 68 - Sets
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct method on line 11 in order to find out the elements of my_set2 that are not members of my_set1.
"""
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

diff = 

print(sorted(list(diff)))
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

diff = my_set2.difference(my_set1) # You can also use 'diff = my_set2 - my_set1'

print(sorted(list(diff)))