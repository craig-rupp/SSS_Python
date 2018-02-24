#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  if n > 0:
    return str * n
  elif n == 0 and str is not '':
    return ''
  else:
    return str