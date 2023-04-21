
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 44 - Lists
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct function on line 10 in order to sort the elements of my_list in ascending order.
"""
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

asc = 

print(asc)
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

asc = sorted(my_list)  #  You can also do 'my_list.sort()' and then print 'my_list'. This will make 'my_list' sort in ascending and no need to store it in any variable. Just print 'my_list'

print(asc)