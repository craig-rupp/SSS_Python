#Check if two arrays passed (a & b) - either have same first or last index, 
#push into new lists to quickly check values
def common_end(a, b):
	beginning = [a[0], b[0]]
	end = [a[-1], b[-1]]
	if beginning[0] == beginning[1] or end[0] == end[1]:
		return True
	else:
		return False

# print(common_end([1, 2, 3], [7, 3]))
# print(common_end([1, 2, 3], [7, 3, 2]))

# moved first index item to end of list, use extend list to pass all values in one argument
def rotate_left3(nums):
  new_list = []
  if len(nums) == 3:
    new_list.extend([nums[1], nums[len(nums) - 1], nums[0]])
    #new_list.append(nums[0])
  return new_list

# print(rotate_left3([1, 2, 3]))

# Reverse String, with step trick in index notation, and through while loop
def reverse3(nums):
  return nums[::-1]

def reverse33(nums):
	n = len(nums) - 1
	new_arr = []
	while n >= 0:
		print(n)
		new_arr.append(nums[n])
		n -= 1
	return new_arr

# print(reverse33([7,8,9,10,11]))

# Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
# and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
	max_value = max(nums[0], nums[-1])
	return [max_value for i in range(len(nums))]

# print(max_end3([11, 5, 9, 14]))


# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, 
# just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
	if len(nums) >= 3 or len(nums) == 2:
		return sum(nums[0:2])
	if len(nums) < 2:
		return sum(nums)

# print(sum2([1,2,3]))
# print(sum2([1,1]))
# print(sum2([1, 1, 1, 1]))
# print(sum2([1]))
# print(sum2([]))

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
	middle_a = float(len(a)) / 2
	middle_b = float(len(b)) / 2
	if middle_a % 2 != 0 and middle_b % 2 != 0:
		return [a[int(middle_a - .5)], b[int(middle_b - .5)]]
	#return [a[1], b[1]]
print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 8, 9, 10]))





  
