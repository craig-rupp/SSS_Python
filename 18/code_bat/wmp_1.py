#Given 2 int values, return True if one is negative and one is positive. 
#Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
  if a <= -1 and b >= 0 and negative is False:
    return True
  elif a >= 0 and b <= -1 and negative is False:
    return True
  elif a <= -1 and b <= -1 and negative is True:
    return True
  else:
    return False
    
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

#Given a string, we'll say that the front is the first 3 chars of the string. 
#If the string length is less than 3, the front is whatever is there. 
#Return a new string which is 3 copies of the front.

def front3(str):
  if len(str) >= 3:
    return str[0:3] * 3
  else:
    return str[0:len(str)] * 3

#Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  if len(str) >= 2:
    return str[-1] + str[1:len(str) -1] + str[0]
  else:
    return str

#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

#Given a string, return a new string where "not " has been added to the front. 
#However, if the string already begins with "not", return the string unchanged.
def not_string(str):
  broken_down = str.split(" ")
  if broken_down[0] == 'not':
    return str
  else:
    return 'not ' + str


# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string 
# (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
  return(str[:n] + str[n+1:])












