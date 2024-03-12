import time
from reloading import reloading


@reloading
def func():
    print("Reloading again")
    print("I'm done")
    time.sleep(10)


for i in range(100):
    func()

