import functools

def my_decorator(function):
    @functools.wraps(function)
    def function_running_argument():
        print("I'm the decorator")
        function()
        print("After the function runs")
    return function_running_argument  ##make sure return statement isn't indented

@my_decorator
def my_function():
    print("I'm the function")

#my_function()

##more advanced decorators

def decorator_with_arg(number):
    def my_decorator_again(func):
        @functools.wraps(func)
        def function_run(*args, **kwargs):
            print("In the decorator")
            if number == 56:
                print("Not running function")
            else:
                func(*args, **kwargs)
            print("After the decorator")
        return function_run
    return my_decorator_again

##my_decorator_again replaces (my_function_too) with function_run, must return function replacing function call and decorator
##decorator

@decorator_with_arg(55)
def my_function_too(x, y):
    print(x + y)
my_function_too(8, 24)
