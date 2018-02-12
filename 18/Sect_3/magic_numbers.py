import random as rd
magic_numbers = [rd.randint(10, 30), rd.randint(10, 30)]


def ask_check():
	user_number = int(input("Make a selection between 10 - 30 : "))
	if user_number in magic_numbers:
		return "Great slection! Your guess {} : matched a magic number!".format(user_number)
	if user_number not in magic_numbers:
		return "Unfortunately your guess {} : is not a magic number".format(user_number)

def run_and_check(chances):
	print("You have {} chances, to make a correct guess".format(str(chances)))
	for attempt in range(chances):
		#print(attempt, chances)
		print("This was attempt, {}".format(attempt + 1))
		print(ask_check())
		if attempt == chances - 1 :
			print("The pair of random numbers were : " + str(magic_numbers))

run_and_check(int(input("Please set your chance amount : ")))
	