import random as rd

numbers_required = 10
random_digits = []
for numbers in range(numbers_required):
	random_digits.append(rd.randint(0, 35))
	print(str(min(float(i) for i in random_digits)) + " : is the lowest generated number")
print(random_digits) 