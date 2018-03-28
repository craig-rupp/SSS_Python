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