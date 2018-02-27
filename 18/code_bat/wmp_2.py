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


def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  print(last2)
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    print(i)
    print(sub)
    if sub == last2:
		count = count + 1
		print('caught')
  return count

#print(last2('hixxhi')) 
#print(last2('axxxaaxx'))

#Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
  count = 0
  if isinstance(nums, (list,)):
    for number in nums:
      if number == 9:
        count += 1
    return count


#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
def array_front9(nums):
  if isinstance (nums, (list,)):
    for index in range(len(nums)):
    	if nums[index] == 9 and index <= 3:
    		return True
    else:
    	return False

#print(array_front9([1, 2, 9, 3, 4]))
#print(array_front9([1, 2, 3, 4, 9]))


#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
	match_sequence = [1, 2, 3]
	for num in range(len(nums)):
		if num < len(nums) - 2:
			sequence = nums[num:num + 3]
			if sequence == match_sequence:
				return True
	return False
			# print(str(num) + ': index')
			# print(str(nums[num]) + ': value')

#print(array123([1, 1, 2, 1, 2, 3]))
#print(array123([1, 1, 2, 4, 1]))

#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
#So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" 
#substrings appear in the same place in both strings.
def string_match(a, b):
	string_check = []
	string_check.extend((a, b))
	count = 0
	#make sure each argument is a string
	for string in string_check:
		if isinstance(string, (basestring,)):
			count += 1
	#if both strings, find shorter string min(len(first arg), len(second arg))
	if count == len(string_check):
		shorter = min(len(a), len(b))
		count = 0
		#loop through shorter string - 1 to 
		print(range(shorter))
		for i in range(shorter - 1):
			#print(range(shorter - 1))
			print(i)
			a_string = a[i : i + 2]
			b_string = b[i : i + 2]
			print(a_string, b_string)
			if a_string == b_string:
				count += 1
		print(str(count) + ': were the total matches')

string_match('xxcaazz', 'xxbaaz')


