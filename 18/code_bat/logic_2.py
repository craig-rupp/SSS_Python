# We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
# Return True if it is possible to make the goal by choosing from the given bricks. 

def make_bricks(small, big, goal):
	if goal >= 5 * big:
		remainder = goal - (5 * big)
	else:
		remainder = goal % 5
	return small >= remainder

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 8))

def lone_sum(a, b, c):
	sum = 0
	sum += a if a not in [b, c] else 0
	sum += b if b not in [a, c] else 0
	sum += c if c not in [a, b] else 0
	return sum
print(lone_sum(1,2,3))
print(lone_sum(3,2,3))


# Given 3 int values, a b c, return their sum. However, if one of the values is 13 
# then it does not count towards the sum and values to its right do not count. 
# So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
	sum_list = [a, b, c, 13]
	sum_total = 0
	for digit in sum_list[:sum_list.index(13)]:
		sum_total += digit
	return sum_total
print(lucky_sum(1, 13, 3))

# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 
# inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper 
# "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, 
# you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the 
# same indent level as the main no_teen_sum().

def no_teen_sum(a, b, c):
  array_check = [13, 14, 17, 18, 19]
  def fix_teen(n):
    return n if n not in array_check else 0
  return sum([fix_teen(a), fix_teen(b), fix_teen(c)])


# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, 
# so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less 
# than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code 
# repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below 
# and at the same indent level as round_sum().

def round_sum(a, b, c):
  def round10(num):
    if num % 10 >= 5:
      return num + 10 - (num % 10)
    return num - (num % 10)
  return sum([round10(a), round10(b), round10(c)])



def close_far(a, b, c):
	# list_of = [a, b, c]
	# return sorted(list_of)
	first_cond = abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a - c) >= 2
	second_cond = abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2
	return first_cond or second_cond



print(close_far(1, 2, 3))
print(close_far(4, 1, 3))


