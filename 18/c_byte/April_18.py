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


