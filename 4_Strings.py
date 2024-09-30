# String has slice and strip methods 
# slice syntax : print(L1[0:5]);
# strip means it cuts the spaces inside the string and input.

# REMEMBER : String is IMMUTABLE that is it can't be changed.
# Replace methods

# Now We need to create list from a string input (It's more of a recurrive tasks)
chai = 'Lemon, Masala, Mint, Ginger'
print(chai.split(", ")) # here, due to split string values into list form but ", " this is deleted.

chai_type = 'Gingers chai'
quanity = 2
Order = "I have Ordered {} cups of {}"   # this {} means placeholders where you add the variables
#  To which we use format methods to insert variables.
print(Order.format(quanity, chai_type))

