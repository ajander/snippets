# See documentation for more info:  
# https://docs.python.org/3/tutorial/modules.html


a = 5
b = 7

### import specific function(s) from script ###

from script1 import add_numbers
from script2 import subtract_numbers

print(add_numbers(a,b))
print(subtract_numbers(a,b))

### import all functions from script ###

# import script1
# import script2 

# print(script1.add_numbers(a,b))
# print(script2.subtract_numbers(a,b))