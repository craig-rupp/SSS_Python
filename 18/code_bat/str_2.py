import fnmatch
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

#print(double_char('hello'))
#print(double_char('The')) #TThhee
#print(double_char('AAbb')) #AAAAbbbb
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

#print(count_hi('hitherehithere hi'))

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

#print(cat_dog('catdog'))
#print(cat_dog('catcatdogcat'))
#print(cat_dog('cat dog dog cat cat'))

lst = ['this', 'is', 'just', 'a', 'test']
#print(fnmatch.filter(lst, 'th?s'))

# Return the number of times that the string "code" appears anywhere in the given string, 
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(string):
	count = 0
	string = string.lower()
	# Have to truncate how many times we loop in order to use + search in index notation
	for i in range(len(string) - 3):
		if string[i : i + 2] == 'co' and string[i + 3] == 'e':
			#print(i, string[i], string[i + 3], i + 3)
			count += 1
	return count

#print(count_code('aaacodebbb'))
#print(count_code('cozexxcope'))


# Given two strings, return True if either of the strings appears at the very end of the other string, 
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
# Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
	long_string, short_string = (a.lower(), b.lower()) if len(a) > len(b) else (b.lower(), a.lower())
	if long_string[-len(short_string) : len(long_string)] == short_string:
		return True
	else:
		return False


print(end_other('Hiabc', 'abc'))


# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded 
# by a period (.). So "xxyz" counts but "x.xyz" does not.
def xyz_there(a):
	string_check = []
	a_list = list(a)
	count = 0
	for i in range(len(a_list)):
		index_check = i + 2
		if a_list[i] == 'x' and a_list[i+1] != 'x' and a_list[i-1] != '.' and index_check < len(a_list):
			print(i, index_check)
			string_check.append(''.join(a_list[i:i+3]))
	print(string_check)
	if 'xyz' in string_check:
		return True
	else:
		return False

#def xyz_again(a):


print(xyz_there('abcxyzxbdxylxy'))
print(xyz_there('xy'))


