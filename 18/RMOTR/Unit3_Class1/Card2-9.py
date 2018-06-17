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