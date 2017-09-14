# Exercise
def who_do_you_know():
    #Ask user for list of people they know, #split string into a list, #return that list
    people_list = input("Please add a list of people you'd like to add to the list : ")
    cleaned_up_list = [peep.strip() for peep in people_list.split(',')]
    print(cleaned_up_list)
    return cleaned_up_list

def ask_user():
    name = input("Please enter a name : ")
    if name in who_do_you_know():
        print("You know, {} was in the list".format(name))
    else:
        print("You know {}, was not in the list".format(name))

who_do_you_know()
# ask_user()





