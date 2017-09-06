my_name = "Craig Rupp"
for letter in my_name: #iterables are strings, lists, sets, tupples and more
    print(letter)


numbers = [4, 8, 3, 9]
for number in numbers:
    print(number ** 2)
    if number % 2 == 0:
        print(str(number) + " : is divisble by two")

user_wants_number = True
while user_wants_number == True:
    print('User wants Number')
    user_input = input("Should we print again? (y/n) ")
    if user_input == 'n':
        user_wants_number = False

