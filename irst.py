import time

def decorator_timer(func):
    def wrapper(number):
        t = time.clock()
        print("time:")
        func(number)
        print(time.clock() - t)
    return wrapper

@decorator_timer
def decorated_function(number):
    number += 1

decorated_function(10)



