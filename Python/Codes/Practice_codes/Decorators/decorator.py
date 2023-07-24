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
        return (func(*args, **kwargs)[:3] + func(*args, **kwargs)[2:3] + "ssss").capitalize()

    return wrap  # returns (name[:3] + name[2:3] + "ssss").capitalize() in this case


# Called the decorator here.
@cutize
def sayName(name):
    return name


## Another way to call a decorator.
## Actually, @decorator calls the same thing as below:
# sayName = cutize(sayName)


# print(sayName("Romit"))   # Prints Rommssss
# print(sayName("Ritik"))   # Prints Rittssss
print(sayName(input("Enter a Name: ")))
