# Tokens are a way to represent pieces of text with meaning to the
# compiler or interpreter. They are the building blocks of source code
# and help the parser understand the structure and semantics of the code.

# Keywords: These are reserved words in a programming language that have
# special meaning.

import math # Import is a keyword
import os

def my_function(): # Def is a keyword
    input_value = input("Enter a number: ")
    return input_value # Return is a keyword

for i in range(20): # For and in are keywords
    val = my_function()
    if val == "": # If is a keyword
        print(i+1)


# Identifiers are names used to *identify* variables, functions, classes, modules, and other objects.

my_variable = 10 # Valid identifier
def calculate_area(radius): # Valid identifier
    area = math.pi * radius ** 2 # Valid identifier
    return area

# Keywords cannot be used as identifiers.

import = 5
def return():
    pass
print(break)


# Operators are special symbols that perform operations on variables and values.

one = 1 # = is an operator, specifically the assignment operator.
two = 2
sum_result = one + two # + is an arithmetic operator. +, -, *, /, %, **, // 
# are all arithmetic operators.


# Literals are fixed values that are directly written into the code.

integer_literal = 42 # Integer literal
float_literal = 3.14 # Floating-point literal.
string_literal = "Hello, World!" # String literal
boolean_literal = True # Boolean literal (True or False)
null_literal = None # Null literal (None in Python)

# There are many more types of literals.


# Punctuation: These are symbols that help structure the code.

list_example = [1, 2, 3, 4] # [] are used for lists
dict_example = {'key': 'value'} # {} are used for dictionaries
tuple_example = (1, 2, 3) # () are used for tuples
function_call = my_function() # () are used for function calls

# They are also related to delimiters, which separate elements in the code.


