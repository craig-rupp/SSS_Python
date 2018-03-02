def double_char(string):
	new_string = ''
	str_arr = list(string)
	for i in range(len(str_arr)):
		if str_arr[i] != str_arr[i + 1]:
			new_string += str_arr[i] * 2
		elif str_arr[i] == str_arr[i + 1]:
			new_string += str_arr[i] * 4
	return new_string


print(double_char('hello'))
print(double_char('The')) #TThhee
print(double_char('AAbb')) #AAAAbbbb
print(double_char('Hi-There')) #'HHii--TThheerree'