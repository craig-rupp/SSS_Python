def double_char(string):
	new_string = ''
	str_arr = list(string)
	for i in range(len(str_arr)):
		if i < len(str_arr) - 1 and str_arr[i] == str_arr[i + 1]:
			new_string += str_arr[i] * 4
		elif i < len(str_arr) - 1 and str_arr[i] != str_arr[i + 1] and str_arr[i] != str_arr[i-1]:
			new_string += str_arr[i] * 2
		elif i == len(str_arr) - 1 and str_arr[i] != str_arr[i - 1]:
			new_string += str_arr[i] * 2
		elif len(str_arr) == 1:
		  new_string += str_arr[i] * 2
	return new_string

print(double_char('hello'))
#print(double_char('The')) #TThhee
print(double_char('AAbb')) #AAAAbbbb
#print(double_char('Hi-There')) #'HHii--TThheerree'


#Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(string):
	str_list = []
	count = 0
	string = "".join(string.split())
	for i in range(len(string)):
		str_list.append(string[i])
	for char in range(len(str_list)):
		 if str_list[char] == 'i' and str_list[char - 1] == 'h':
		 	count += 1
	return count

print(count_hi('hitherehithere hi'))


#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(string):
	arg_string = []
	dog = 0
	kitty = 0
	string = "".join(string.split())
	for char in range(len(string)):
		arg_string.append(string[char])
	for char in range(len(arg_string)):
		if arg_string[char] == 't' and arg_string[char - 1] == 'a' and arg_string[char - 2] == 'c':
			kitty += 1
		elif arg_string[char] == 'g' and arg_string[char - 1] == 'o' and arg_string[char - 2] == 'd':
			dog += 1
	if dog == kitty:
		return True
	if dog != kitty:
		return False		

print(cat_dog('catdog'))
print(cat_dog('catcatdogcat'))
print(cat_dog('cat dog dog cat cat'))

