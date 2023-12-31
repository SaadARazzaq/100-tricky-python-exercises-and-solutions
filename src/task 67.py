
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 67 - Sets
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct method on line 11 in order to join the elements of my_set1 and my_set2.
"""
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

join = 

print(sorted(list(join)))
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

join = my_set1.union(my_set2)  # You can also use 'join = my_set1 | my_set2'

print(sorted(list(join)))