def methodception(another):
    print(another())

def add_two():
    return 100+1

methodception(add_two)

methodception(lambda: 35 + 77)

my_list = [13, 37, 74, 19]
print(list(filter(lambda x: x != 74, my_list))) ##must encapsulate with list to return list

print((lambda x: x * 3)(5)) #look below for method like translation

print([x for x in my_list if x != 13]) ##list compr

#translates to
# def above(x):
#     return x * 3;
# above(5)
