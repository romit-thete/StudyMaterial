"""
Refer: https://www.geeksforgeeks.org/decorators-in-python/ for more
"""


# Decorator to say cute names
# Define using a function having a wrapper function
def cutize(func):
    # Wrapper function is needed for the decorator.
    # *args and **kwargs are passed so that arguments from the
    # funcs using them are also used by the decorator!
    def wrap(*args, **kwargs):
        # Changed_Here: removed .capitalize()
        return func(*args, **kwargs)[:3] + func(*args, **kwargs)[2:3] + "ssss"

    return wrap  # returns (name[:3] + name[2:3] + "ssss") in this case


# Creating another decorator which would simply return the strings in uppercase
def shout(func):
    def wrap(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrap


# Called the decorators here.
# Note: The sequence matters here, if cutize comes first and then shout,
# the results might appear different from what we could see in the below case.
# The decorator closer to the function definition is called first (try reversing the order)
# Also, Try commenting out @cutize and see what heppens!
@shout
@cutize
def sayName(name):
    return name


# print(sayName("romit"))  # Prints ROMMSSSS
# print(sayName("Ritik"))  # Prints RITTSSSS
print(sayName(input("Enter a Name: ")))
