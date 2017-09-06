a = 5
b = 10
my_variable = 56

string_variable = "hello"
string_singular = 'singular quotes work too'

# print(my_variable, a, b)

##

def my_print_method(x, y):
    print("Your number " + str(x) + " has an " + str(y) + " in it")

my_print_method(my_variable, a)

def my_multiple_method(number_one, number_two):
    print((number_one * number_two) / 5)
    ##can't use with other method, must return

def return_multiples(one_num, two_num):
    return (one_num * two_num) / 3

my_multiple_method(a, b)
my_multiple_method(15, 100)
this_result = return_multiples(a, b)
print(this_result)
my_print_method(return_multiples(a, b), 10)