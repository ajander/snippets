a = 5
b = 7

### import specific function(s) from script ###

# from helpers.addition_helper import add_numbers
# from helpers.subtraction_helper import subtract_numbers

# print(add_numbers(a,b))
# print(subtract_numbers(a,b))

### import all functions from script ###

import helpers.addition_helper as ah
import helpers.subtraction_helper as sh 

print(ah.add_numbers(a,b))
print(sh.subtract_numbers(a,b))