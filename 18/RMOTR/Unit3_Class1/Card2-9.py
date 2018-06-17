# Write a function create_box that takes three inputs: height (rows), width (columns), 
# and a character char and creates a height × width box using the character char.

# For this exercise, it's recommended to use a nested for-loop. 
# There are other ways of solving it (which might be a good starting point), 
# but try reaching the nested for-loop solution.

def create_box(height, width, char):
    box = ''
    for i in range(height):
        row = ''
        for l in range(width):
            row += char
        box += row + '\n'
    return box
print(create_box(3, 4, '*'))
print(create_box(2, 2, '@'))

# Expand on the last assigment and write a function create_empty_box that takes three inputs: 
# height (rows), width (columns), and a character char and creates a height × width box using the character 
# char that only has characters on the borders of the box (it's not filled in).

# If the box height or width are less than 3, return 'Invalid box dimensions' because 
# it won't be an empty box.

def create_empty_box(height, width, char):
    if height < 3 or width < 3:
        return 'Invalid box dimensions'
    else:
        box = ''
        first_last = [0, height - 1]
        for i in range(height):
            row = ''
            for l in range(width):
                if i in first_last:
                    row += char 
                else:
                    col_first_last = [0, width - 1]
                    if l in col_first_last:
                        row += char
                    else:
                        row += ' '
            box += row + '\n'
        return box 
print(create_empty_box(3, 4, '*'))

# Write a function nested_pyramid that receives a number height 
# and a character char and builds an ASCII Pyramid with them. Examples:

def nested_pyramid(height, char):
    pyr = ''
    for i in range(1, height + 1):
        row = ''
        for l in range(i):
            row += char
        pyr += row + '\n'
    return pyr
print(nested_pyramid(5, '*'))
print(nested_pyramid(3, '#'))


# Extend your previous solution to include a third parameter "order" which can be either "ASC" or "DESC. 
# Depending of the order provided, the pyramid will be displayed in ascending order ("ASC") or descending 
# order ("DESC"). Examples:

def advanced_nested_pyramid(height, char, order):
    pym = ''
    for i in range(1, height + 1):
        row = ''
        if order == 'ASC':
            row_length = i 
        else:
            row_length = (height + 1) - i 
        for l in range(row_length):
            row += char 
        pym += row + '\n'
    return pym 
print(advanced_nested_pyramid(5, '#', 'ASC'))
#print(advanced_nested_pyramid(5, '@', 'DESC'))

# Basically, all the elements in the diagonal are ones (1s) and the rest are zeros (0s).

# An identity matrix has a size associated. For example, this is an identity matrix of size 3:

# 1 0 0
# 0 1 0
# 0 0 1

# size 3
# size_3_matrix = [
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1],
# ]
# # size 5
# size_5_matrix = [
#     [1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
# ]

def identity_matrix(size):
    master_list = [[] for _ in range(size)]
    iterator_last = len(master_list) + 1 
    for i in range(1, iterator_last):
        for l in range(1, iterator_last):
            if l == i:
                master_list[i - 1].append(1)
            else:
                master_list[i - 1].append(0)
    return master_list
print(identity_matrix(3))


# Use the random module (more below) to write a function random_matrix that returns a matrix size m × n with 
# random numbers (m is the number of rows and n is the number of columns).
# The only restriction is that elements in the matrix CAN'T be repeated, they must be unique. 
# Examples:

import random

def random_matrix(m, n):
    lists = [[] for _ in range(m)]
    for i in range(m):
        for l in range(n):
            def generate():
                rand_int = random.randint(1, 1000)
                if rand_int in lists:
                    generate()
                else:
                    return rand_int
            lists[i].append(generate())
    return lists
print(random_matrix(3, 2))

# For this assignment, we'll rewrite the builtin function zip, it's going to be called rmotr_zip. rmotr_zip receives two collections (lists, tuples, doesn't matter) and must "zip" their elements. Zip just means matching elements in the same positions for both collections. A conceptual example of zip:

# collection_a = ['A', 'B', 'C', 'D']
# collection_b = [ 1 ,  2 ,  3 ,  4 ]

# # Zip collection_a and collection_b means:

# 'A' => 1
# 'B' => 2
# 'C' => 3
# 'D' => 4
def rmotr_zip(collection_a, collection_b):
    if len(collection_a) != len(collection_b):
        return None
    else:
        collections = []
        a = collection_a
        b = collection_b
        for i in range(len(a)):
            collections.append((a[i], b[i]))
        return collections
print(rmotr_zip(['A', 'B', 'C'], [1, 2, 3]))



# Each state contains a list with all the customers. A single customer is represented 
# as a dictionary with only two keys, name and age.

# Write a function number_of_customers_per_state that receives a customers dictionary 
# and calculates the number of customers per state. The result will be a new dictionary, 
# with each key containing a state and the count as the associated value.

def number_of_customers_per_state(customers_dict):
    result = {}
    for key, value in customers_dict.items():
        if value:
            for i in range(len(value)):
                result.setdefault(key, 0)
                result[key] += 1
        else:
            result[key] = 0
    return result
customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',
        'age': 31
    }, {
        'name': 'Robert',
        'age': 16
    }],
    'NY': [{
        'name': 'Linda',
        'age': 71
    }],
    'CA': [{
        'name': 'Barbara',
        'age': 15
    }, {
        'name': 'Paul',
        'age': 18
    }]
}
print(number_of_customers_per_state(customers))


# With the same structure as before, now you need to write a 
# function that finds the eldest customer per state.

def eldest_customer_per_state(customers_dict):
    eldest_hopefully = {}
    for key, value in customers_dict.items():
        if len(value) >= 1:
            eldest_hopefully[key] = max(value, key=lambda x:x['age'])
        else:
            eldest_hopefully[key] = None
    return eldest_hopefully
print(eldest_customer_per_state(customers))

