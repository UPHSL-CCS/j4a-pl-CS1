# Semantic errors occur when the code is syntactically correct,
# but the logic or meaning behind the code is flawed. This means
# that the code can be executed, but it doesn't do what the programmer
# intended it to do.

a = 5
b = 0
c = a / b
print("Result:", c) 

# While syntax-wise this code is correct, it will raise a runtime error
# because dividing by zero is undefined.
# This makes semantic errors harder to catch, as they often
# only become apparent during execution.

# More examples with not-as-glaring errors:

list1 = [1, 2, 3]
print(list1[3])  
# ERROR: Index 3 is out of range for list1. (The indices available are 0, 1, and 2.)

name = "Alice"
print("Hello, " + name + "! You are " + age + " years old.")
# ERROR: The program does not know what 'age' is, because the programmer
# forgot to define it or assign a value to it before using it.