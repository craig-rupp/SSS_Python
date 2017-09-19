def my_method(arg1, arg2):
    return arg1 * arg2

def my_list_addition(arg_arr):
    return sum(arg_arr)

def add_simplified(*args):
    print(sum(args))

add_simplified(10, 10, 15, 35)

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12, 34, 56, name='Craig', location='Albuquerque')