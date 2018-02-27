#Given an "out" string length 4, such as "<<>>", and a word, 
#return a new string where the word is in the middle of the out string, e.g. "<<word>>".
def make_out_word(out, word):
  if len(out) == 4:
    return out[0 : 2] + word + out[2:len(out)]
  else:
    return False

#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
#The string length will be at least 2.
def extra_end(str):
  return str[-2:len(str)] * 3


# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", 
# and the empty string "" yields the empty string "".
def first_two(str):
  if len(str) >= 2:
    return str[0:2]
  else:
    return str[:len(str)]

#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(string):
  #length = len(string)
  if len(string) % 2 == 0:
    #return 'Hey ' + str(len(string))
    return string[:(len(string) / 2)]


#print(first_half('WooHoo'));
#print(first_half('HelloThere'))

#Given a string, return a version without the first and last char, so "Hello" yields "ell". 
#The string length will be at least 2.
def without_end(str):
  if len(str) >= 3:
    return str[1:-1]
  else:
    return ''


# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside 
# and the longer string on the inside. The strings will not be the same length, 
# but they may be empty (length 0).

#****The min function has an optional parameter key that lets you specify a function to determine the "sorting value"
#*** of each item. We just need to set this to the len function to get the shortest value:

def combo_string(a, b):
	string_check = []
	count = 0
	string_check.extend((a, b))
	for string in string_check:
		if isinstance(string, (basestring,)):
			count += 1
	if len(string_check) == count and len(a) != len(b):
		short_string = min(string_check, key=len)
		long_string = max(string_check, key=len)
		return short_string + long_string + short_string

print(combo_string('Hello', 'hi'))



# Given 2 strings, return their concatenation, 
# except omit the first char of each. The strings will be at least length 1.
def non_start(a, b):
	return a[1:len(a)] + b[1:len(b)]


print(non_start('Hello', 'There'))


#Given a string, return a "rotated left 2" 
#version where the first 2 chars are moved to the end. The string length will be at least 2.
def left2(str):
  if len(str) == 2:
    return str
  else:
    return str[2:len(str)] + str[0:2]




