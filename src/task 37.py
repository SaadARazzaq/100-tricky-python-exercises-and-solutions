
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 37 - Lists
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct code on line 10 in order to remove the element of my_list located at index 5.
"""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.

print(my_list)
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.remove(my_list[5])  #  You can also use 'my_list.pop(5)'

print(my_list)