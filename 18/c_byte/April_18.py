def LetterCountI(str): 
    str_list = str.split(' ')
    str_object = {}
    for index, value in enumerate(str_list):
        str_object[index] = 0
        for i in range(len(str_list[index])):
            if value.count(value[i]) >= 2:
                str_object[index] += 1
    maximum = max(str_object, key=str_object.get)
    #return [maximum, str_object]
    if maximum == 0 and str_object[maximum] == 0:
        return -1
    else:
        return str_list[maximum]
    
#print LetterCountI(raw_input())

def ArrayAdditionI(arr):
    max_value = (max(arr))
    del arr[arr.index(max(arr))]
    power_set = [[]]
    for i in range(len(arr)):
        for j in range(len(power_set)):
            temp = [arr[i]] + power_set[j]
            power_set.append(temp)
            if sum(temp) == max_value:
                return 'true'
    return 'false'
#print ArrayAdditionI(raw_input())

def DivisionStringified(num1,num2): 
    value = round(float(num1)/float(num2))
    value_list = list(str(value))
    if value_list.index('.') <= 3:
        return ''.join(value_list[:value_list.index('.')])
    else:
        value_list = list(str(int(value)))
        comma_check = 0
        for i, e in reversed(list(enumerate(value_list))):
            comma_check += 1
            #print(comma_check, [i, e])
            if comma_check == 3:
                value_list[i] = ',' + e
                comma_check = 0
    return ''.join(value_list)
            
#print DivisionStringified(raw_input())


def CountingMinutesI(str): 
    time_arr = str.split('-')
    first_time = time_arr[0].split(':')
    first_min = (int(first_time[0]) * 60) + int(first_time[1][:2])
    first_tz = first_time[1][2:]
    second_time = time_arr[1].split(':')
    second_min = (int(second_time[0]) * 60) + int(second_time[1][:2])
    second_tz = second_time[1][2:]
    
    difference = second_min - first_min
    if first_tz != second_tz:
        difference += (12 * 60)
    elif first_min >= second_min:
        difference += (24 * 60)
    return difference
#print CountingMinutesI(raw_input())

def to_minutes(s):
    t = [int(t) for t in s[:-2].split(':')]
    print(t)
    if s.endswith('pm'):
        t[0] += 12
    return t[0] * 60 + t[1]

def CountingMinutes(string):
    mins = [to_minutes(t) for t in string.split('-')]
    print(mins)
    res = mins[1] - mins[0]
    if res < 0:
        res = 24 * 60 + res
    return res


#print(CountingMinutes("12:15pm-12:25am"))

def MeanMode(arr): 
    mode = max(arr, key=arr.count)
    mean = sum(arr) / len(arr)
    return 1 if mode == mean else 0
#print MeanMode(raw_input())

def secondMeanMode(arr): 
  mean = float(sum(arr)/len(arr))
  nmode = max([arr.count(i) for i in arr])
  for i in arr:
    if arr.count(i) == nmode:
      mode = i
  print(mode)
  return 1 if mean == mode else 0

#print(secondMeanMode([1, 5, 3, 3, 4, 2]))
#print(secondMeanMode([1, 2, 2, 3, 1]))

def DashInsert(s):
    new_string = ' '
    for char in range(len(s)):
        if char <= len(s) - 2 and int(s[char]) % 2 != 0 and int(s[char + 1]) % 2 != 0:
            new_string += s[char] + '-'
        else:
            new_string += s[char]
    return new_string        
#print DashInsert(raw_input())

def SwapCase(s):
    new_string = ''
    for char in range(len(s)):
        if s[char].isalpha():
            if s[char].isupper():
                new_string += s[char].lower()
            else:
                new_string += s[char].upper()
        else:
            new_string += s[char]
    return new_string
#print SwapCase(raw_input())

def swap(ch):
  return ch.lower() if ch.isupper() else ch.upper()

def SwapCase(s): 
  return ''.join([swap(ch) for ch in s])


def NumberAddition(s): 
    s_obj = {}
    for char in range(len(s)):
        if s[char].isdigit():
            s_obj[char] = s[char]
    n_str = ''
    n_arr = [x for x in s_obj]
    for i in range(len(n_arr)):
        for j, k in s_obj.items():
            #print(i, n_arr[i], j, k)
            if i == j:
                n_str += str(k)
            elif n_arr[i] == j and j != i:
                n_str += ' {}'.format(str(k))
    return sum(map(int, n_str.split(' ')))
        
        #fun but not a great solution (and easily broke 3 out of 5)
print NumberAddition("Won90 8")   

def NumberAddition(s): 
    n2 = ''.join([str(i) if i.isdigit() else ' ' for i in list(s)]).split(' ')
    just_n = list(filter(lambda x: x != '', n2))
    return sum([int(x) for x in just_n])
#print NumberAddition(raw_input())

def ThirdGreatest(strArr): 
    return sorted(strArr, key=len, reverse=True)[2]
#print ThirdGreatest(raw_input())

def PowersofTwo(num): 
    return 'true' if bin(num).count('1') == 1 else 'false'
#print PowersofTwo(raw_input())

def AdditivePersistence(num):
    arr = list(str(num))
    while len(arr) > 1:
        combined = 0
        for i in range(len(arr)):
            combined += int(arr[i])
        return 1 + AdditivePersistence(combined)
    return 0
#print AdditivePersistence(raw_input())
# This is a sweet recursive function! - take the num parameter being passed which will always be a 
# positive integer and return its additive persistence which is the number of times you must add the 
# digits in num until you reach a single digit.

def MultiplicativePersistence(num): 
    num_list = list(str(num))
    count = reduce(lambda x, y: int(x)*int(y), num_list)
    if len(num_list) >= 2:
        return 1 + MultiplicativePersistence(count)
    else:
        return 0 
#print MultiplicativePersistence(raw_input())
# Similar to above, need to look at reduce more

def OffLineMinimum(strArr):
    new_str = []
    for i in range(len(strArr)):
        if strArr[i] == 'E':
            temp = min(strArr[:i])
            if temp not in new_str:
                new_str.append(temp)
            elif temp in new_str:
                new_arr = list(filter(lambda x: x != 'E' and x not in new_str, strArr[:i]))
                new_str.append(sorted(new_arr)[0])
    return ','.join(new_str)
#print OffLineMinimum(raw_input())







