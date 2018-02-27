#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  if n > 0:
    return str * n
  elif n == 0 and str is not '':
    return ''
  else:
    return str

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  return str[::2]

#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
	new_string = ''
	for character in range(len(str)):
		print(character)
		new_string += str[:character+1]
		print(new_string + '\n')

#string_splosion('code');

# Given a string, return the count of the number of times that a substring length 2 
# appears in the string and also as the last 2 chars of the string, 
# so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
	count = 0
	last_2 = str[len(str) - 2 :]
	for character in range(len(str)):
		string_check = str[character : character + 2]
		if len(str) > 2 and string_check == last_2 and character < (len(str) - 2):
			count += 1
	return count


# def last2(str):
#   # Screen out too-short string case.
#   if len(str) < 2:
#     return 0
  
#   # last 2 chars, can be written as str[-2:]
#   last2 = str[len(str)-2:]
#   print(last2)
#   count = 0
  
#   # Check each substring length 2 starting at i
#   for i in range(len(str)-2):
#     sub = str[i:i+2]
#     print(i)
#     print(sub)
#     if sub == last2:
# 		count = count + 1
# 		print('caught')
#   return count

#print(last2('hixxhi')) 
print(last2('axxxaaxx'))


