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


def SimpleSymbols(string): 
    string_list = list(string)
    if string_list[0].isalpha() or string_list[len(string_list)-1].isalpha():
        return False
    for i, l in enumerate(string_list):
        if l.isalpha():
            if string_list[i-1] != '+' or string_list[i+1] != '+':
                return False
    return True
print SimpleSymbols(raw_input())

def FirstFactorial(n):
    if n >= 1 : 
        num = 1
        while n >= 1:
            num = n * num
            n = n - 1
        return num
    else :
        return 1
# keep this function call here  
print FirstFactorial(int(raw_input()))
