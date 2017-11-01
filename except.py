def ignore_exceptions(exception_name):
    def decorator(func):

        def wrapped(number1, number2):
            try:
                func(number1, number2)
            except exception_name:
                print("None")
            else:
                print(func(number1,number2))
        return wrapped
    return decorator

@ignore_exceptions(ZeroDivisionError)
def counter(number1, number2):
    return number1/number2

counter(5, 5)



