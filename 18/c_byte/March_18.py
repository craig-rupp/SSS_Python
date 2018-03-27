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

#Output passed num into format of 'hour:minutes'
def TimeConvert(num): 
    hour = ''
    minutes = int
    if num >= 60:
        hour = str(int(round(num/60)))
        minutes = num - (int(hour) * 60)
    else:
        hour = '0'
        minutes = num
    return '{}:{}'.format(hour, str(minutes))
# keep this function call here  
#print TimeConvert(raw_input())

#Return string argument in alphabetical order
def AlphabetSoup(str): 
    return ''.join(sorted(list(str)))
# keep this function call here  
#print AlphabetSoup(raw_input())

# have the function ABCheck(str) take the str parameter being passed and return the string 
# true if the characters a and b are separated by exactly 3 places anywhere in the string at least 
# once (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). 
# Otherwise return the string false. 
def ABCheck(str): 
    str_list = list(str)
    b_check = []
    for i in range(len(str_list)):
        if str_list[i] == 'a' and i < (len(str_list)-4):
            b_check.append(str_list[i + 4])
        if str_list[i] == 'a' and i >= 4:
            b_check.append(str_list[i-4])
    return 'true' if 'b' in b_check else 'false'
print ABCheck(raw_input().lower())


def Palindrome(string): 
    if string.count(' ') < 1:
        return 'true' if string[::-1] == string else 'false'
    else:
        string_list = list(string)
        reverse_string_arr = [x for x in string_list[::-1] if x != ' ']
        string_w_space_index = [index for index, value in enumerate(string_list) if value == ' ']
        adjusted_index = []
        for i in range(len(string_w_space_index)):
            if i < 1:
                adjusted_index.append(string_w_space_index[i])
            else:
                adjusted_index.append(string_w_space_index[i] - i)
        backwards_string = ''
        for char in range(len(reverse_string_arr)):
            if char in adjusted_index:
                backwards_string += ' ' + reverse_string_arr[char]
            else:
                backwards_string += reverse_string_arr[char]
    return 'true' if backwards_string == string else 'false'
#print Palindrome(raw_input())

def Palindrome(string):
    arg_string = ''.join([x for x in string[::] if x != ' '])
    check_string = ''.join([x for x in string[::-1] if x != ' '])
    return 'true' if arg_string == check_string else 'false'
#print Palindrome(raw_input())



