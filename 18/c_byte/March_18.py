# Input:"I Love Code" : Output:"edoC evoL I"
def FirstReverse(str): 
	new_str = ''
	n = len(str) - 1
	while n >= 0:
		new_str += str[n]
		#print(new_str)
		n -= 1
	return new_str     
    	
# print FirstReverse('hello friend')  
# print FirstReverse('I Love Code!')  


def SimpleSymbols(string): 
    string_list = list(string)
    if string_list[0].isalpha() or string_list[len(string_list)-1].isalpha():
        return False
    for i, l in enumerate(string_list):
        if l.isalpha():
            if string_list[i-1] != '+' or string_list[i+1] != '+':
                return False
    return True
#SimpleSymbols(raw_input())

def SimpleSymbols(string): 
    if string[0].isalpha() or string[len(string)-1].isalpha():
        print('hello')
        return 'false'
    string_list = list(string)
    for i, l in enumerate(string_list):
        if l.isalpha():
            if string_list[i-1] != '+' or string_list[i+1] != '+':
                print('goodbye')
                return 'false'
    return 'true'

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
# print FirstFactorial(int(raw_input()))

def LongestWord(sen): 
    # code goes here
    sen_array = sen.split(' ')
    return max(sen_array, key=len)
    
# keep this function call here  
#print LongestWord(raw_input())

def LetterCapitalize(string): 
    str_array = string.split(' ')
    new_string = ''
    for word in str_array:
        new_string += word[0].upper() + word[1:] + ' '
    return new_string
# keep this function call here  
#print LetterCapitalize(raw_input())


def LetterChanges(string):
    string_lower = string.lower()
    new_string = []
    for i in range(len(string_lower)):
        for l in string_lower[i]:
            if ord(l) >= 97 and ord(l) <= 121:
                new_string.append(chr(ord(l)+1))
            else:
                new_string.append(l)
    for n, i in enumerate(new_string):
        if i in ['a', 'e', 'i', 'o', 'u']:
            new_string[n] = i.upper()
    return ''.join(new_string)
    
# keep this function call here  
#print LetterChanges(raw_input())

def CheckNums(num1,num2): 

    if num1 == num2:
        return '-1'
    sol = 'true' if num2 > num1 else 'false'
    return sol






