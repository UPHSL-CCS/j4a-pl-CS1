# Variables in programming are used to store data, or other values.
# These variables are used in many ways, and depending on the language they
# have a specific type.

name = "Nicole" # String variable
group = 1
groupmates = ["Nicole", "Kyle", "Jerome", "Junell"] # List variable
is_tired = True # Boolean variable

# Variables have scope, meaning that there are certain areas of the code where they can be used.
# A global scope means that the variable is accessible anywhere.
# Global variables are defined in the main body of the code.

def greet():
    print("Hello, " + name + "!")  # 'name' is accessible here because it's in the global scope.

# Local variables are defined inside a function and can only be used inside that function.

def introduction():
    get_name = input("What is your name? ")  # 'get_name' is a local variable.
    return get_name # It is possible to use get_name elsewhere through the return statement.

print(introduction())

