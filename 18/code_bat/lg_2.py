# Given a non-negative number "num", return True if num 
# is within 2 of a multiple of 10. Note: (a % b) is the remainder of 
# dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
def near_ten(num):
	#print(num % 10)
    return not(2 < (num % 10) < 8)

# print(near_ten(13))
# print(near_ten(18))

# Return the number of even ints in the given array. Note: the % "mod" 
# operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count += 1
  return count

def big_deff(nums):
	minim = min(nums)
	maxim = max(nums)
	num_list = [maxim, minim]
	return num_list

#print(big_deff([2, 10, 7, 2]))



# Return the "centered" average of an array of ints, which we'll
# say is the mean average of the values, except ignoring the largest 
# and smallest values in the array. If there are multiple copies of the smallest value, 
# ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
# You may assume that the array is length 3 or more.
def centered_average(nums):
	#new_list = [i for i in nums if i not in min(nums) or max(nums)]
	nums.remove(min(nums))
	nums.remove(max(nums))
	return int(sum(nums) / len(nums))

#print(centered_average([1, 1, 5, 5, 10, 8, 7]))

# Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that come 
# immediately after a 13 also do not count.
def sum13(nums):
  new_arr = []
  n = 0
  while n < len(nums):
    if nums[n] != 13:
    	new_arr.append(nums[n])
    	n += 1
    else:
    	n += 2
  return sum(new_arr)

#print(sum13([13, 1, 2, 13, 2, 1, 13]))

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
# and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum67(nums):
	stop_flag = True
	total = 0
	for num in nums:
		if num != 6 and stop_flag == True:
			total += num 
		elif num == 6:
			stop_flag = False
		elif stop_flag == False and num == 7:
			stop_flag = True
	return total
	#(Only works for one 6)
	# if 6 in nums:
	# 	return sum(nums[:nums.index(6)] + nums[nums.index(7) + 1 :])
	# elif 6 not in nums and len(nums) >= 1:
	# 	return sum(nums)
	# elif len(nums) == 0:
	# 	return 0

#print(sum67([1, 1, 6, 7, 2]))
#print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))

#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
	for i in range(len(nums)):
  		if nums[i] == 2 and i < len(nums) - 1 and nums[i + 1] == 2:
  			return True
  	else:
  		return False

print(has22([2, 1, 2]))
print(has22([1, 2, 1, 2]))
print(has22([1, 2, 2]))

# my_list = ['one', 'two', 'three', 'four', 'five']
# my_list_len = len(my_list)
# for i in range(my_list_len):
# 	print(my_list[i])
