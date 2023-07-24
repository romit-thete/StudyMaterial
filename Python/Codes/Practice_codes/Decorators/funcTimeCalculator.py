"""
Refer: https://www.geeksforgeeks.org/decorators-in-python/ for more
"""


import time
import math


# Decorator to calculate time taken by a function to execute
# It is very useful when we have larger functions would be helpful for performance improvement.
def calculate_time(func):
    def wrap(*args, **kwargs):
        # Capturing the start time
        begin = time.time()

        # Running the function and printing the output to the user
        # can also remove print and just execute the code if user is not involved here.
        print(func(*args, **kwargs))

        # Capturing the end time
        end = time.time()
        return "Total time taken by the {} function: {}".format(func.__name__, (end - begin))

    return wrap


# Removing the decorator would just compute the factorial and return the result!
# We give a sleep time using time.sleep() so that some delay is introduced.
@calculate_time
def factorial(num):
    time.sleep(2)
    return "Factorial of {} is {}".format(num, math.factorial(num))


print(factorial(5))
