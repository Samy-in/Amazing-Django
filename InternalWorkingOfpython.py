# Internal working in python is based on datatypes.
# In python datatype is assigned to the memory allocation of that value And not the Variable that holds the values.
# Example: 10 is defined as integer and its stored in variable called "Score" this doesn't means that Score is also 
# An integer . NOOOOOO Wrong
# Python doesn't have any datatype but The reference in memory has a datatype.
# 
# When it Comes to integer ans strings , python doesn't delete the numbers or string immediately but it wait a little bit
# Therefore garbage Collection in python is not immediate when it comes to integers, and Strings.
# Remember : "Lists are mutable means it can changes reference on the spot."
L1 = [1,2,3,4]
L2 = L1
# L1 & L2 mein same hai values. 
L1[0] = 33  # now the element in the list is changed And so does the element in the L2 list.
print(L1)
print(L2)

#  But now if we set the L2 values fixed then it won't change 
L2 = [1,2,3,4]
print(L2)

#  Now In python we use Slice function by " Enter the Starting no(n) : Ending no(n-1)"
#  L1 has 3 values from 0 to 3 then if we write
L2 = L1[0:2]     # Ans is 33,2 by Slice function means( 0 ,1 ), 2-1 = 1
print(L2)