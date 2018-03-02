# Input:"I Love Code" : Output:"edoC evoL I"
def FirstReverse(str): 
	new_str = ''
	n = len(str) - 1
	while n >= 0:
		new_str += str[n]
		#print(new_str)
		n -= 1
	return new_str     
    	
print FirstReverse('hello friend')  
print FirstReverse('I Love Code!')  


