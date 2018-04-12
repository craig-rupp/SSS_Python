def ArithGeo(arr): 
    Arith, Geo = True, True
    arith_value = arr[len(arr) - 1] - arr[len(arr)-2]
    geo_value = arr[len(arr)-1] / arr[len(arr)-2]
    n = len(arr)-1
    while n > 0:
        if arr[n] - arr[n-1] != arith_value:
            Arith = False
        if arr[n] / arr[n-1] != geo_value:
            Geo = False
        n -= 1
    return "Arithmetic" if Arith else "Geometric" if Geo else -1
#print ArithGeo(raw_input())

def ArithGeo(arr): 
  rtn = '-1'
  l = len(arr)
  if (l < 2):
    return rtn
  d = arr[1] - arr[0]
  r = arr[1] / arr[0]
  ba = 1
  bg = 1
  for i in range(1,l):
    if (arr[i] != arr[i-1]+d):
      ba = 0
    if (arr[i] != arr[i-1]*r):
      bg = 0
  if (ba == 1):
    return 'Arithmetic'
  if (bg == 1):
    return 'Geometric'
  return rtn
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
#print ArithGeo(raw_input())

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
        
        
print NumberAddition("Won90 8")   

































  