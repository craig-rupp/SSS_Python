#User can pick 6 numbers 
#Lottery calculates 6 random numbers 
#Match user numbers to lottery numbers
#Calculate winnings based on how many numbers the user has entered
import random as rd

def menu():
	#ask player for numbers
	user_numbers = get_player_numbers()
	#calculate lottery numbers
	lotto_numbers = create_lotto_numbers()
	#print out winning numbers
	print(matching_numbers(user_numbers, lotto_numbers)) 

def get_player_numbers():
	number_csv = raw_input("Enter your 6 numbers separated by a comma : ")
	# Create set of integers from above variable
	number_set = set(int(number) for number in number_csv.split(","))
	return number_set
# print(get_player_numbers())

def create_lotto_numbers():
	#Create 6 random Lottery numbers to be held in a set
	#random_lottery_set = {rd.randint(0, 35) for number in range(6)}
	random_lottery_set = set()
	while len(random_lottery_set) < 6:
		random_lottery_set.add(rd.randint(0, 35))
	return random_lottery_set
#print(create_lotto_numbers())

def matching_numbers(first, second):
	matching = first.intersection(second)
	if len(matching) >= 1:
		return "Congrats! You matched {}, and won ${}, 100 ^{}, the amount of matching numbers!".format(matching, 100 ** len(matching), str(len(matching))) 
	return "No matching numbers : sorry :("

menu()
