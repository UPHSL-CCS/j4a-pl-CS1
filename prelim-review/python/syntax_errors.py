# Syntax errors occur when the written code violates
# the language's grammatical rules. This causes the code
# to fail execution, because the compiler/parser cannot understand 
# how to do it.

x = 10
print x;

# If the code above is executed, it will result in an error.
# A correct print statement in Python written as print().

# More code with glaring errors is as follows:

print(y) # ERROR: Cannot use variable before it is declared.

print x; # ERROR: Missing parentheses in the keyword.

def myFunction: # ERROR: Missing parentheses in the function name.
    y x + 1 # ERROR: Missing assignment operator.
    retur y # ERROR: Misspelled keyword.

2x = 11 # ERROR: Variable name invalid because it starts with a number.

