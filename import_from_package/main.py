a = 5
b = 7

### import specific function(s) from script ###

# from helpers.script1 import add_numbers
# from helpers.script2 import subtract_numbers

# print(add_numbers(a,b))
# print(subtract_numbers(a,b))

### import all functions from script ###

import helpers.script1 as s1
import helpers.script2 as s2 

print(s1.add_numbers(a,b))
print(s2.subtract_numbers(a,b))