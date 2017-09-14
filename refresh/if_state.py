should_continue = True
if should_continue:
    print(should_continue)

known_people = ["Craig", "John", "Elizabeth"]
print(known_people)
person = input("Enter the person you know : ")

if person in known_people:
    print("You know, " + person + ", is in our list")
else :
    print("I'm sorry, {}, is not in our list".format(person))

# if person not in known_people:
#     print("I'm sorry, " + person + ", was not in the known list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice == "q":
        return "Quit"