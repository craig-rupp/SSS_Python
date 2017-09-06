grades = [76, 87, 98, 87, 99, 83]
print(sum(grades) / len(grades))
total = 0
for i, grade in enumerate(grades):
    total += grade
    print(total)
print(total/len(grades))
tuple_grades = (75, 65, 35, 23, 29) #immutable
print(tuple_grades)
set_grades = {75, 68, 91, 25, 34, 18} #unique & unordered (will delete any duplicate grades)
print(set_grades)

## Set Operations
print('Set Operations')
your_lotto= {1, 2, 3, 4, 5, 17, 16}
winning_numbers = {3, 8, 11, 17, 29, 16, 87}

print(your_lotto.intersection(winning_numbers))
print(your_lotto.union(winning_numbers)) #add sets and indexes as long as unique (no duplicates)

print(your_lotto.difference(winning_numbers))
print(winning_numbers.difference(your_lotto))

new_set = {14, 5, 9, 31, 12, 77, 67, 8}
this_set = {13, 12, 5, 9, 67}
print(new_set.intersection(this_set))