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