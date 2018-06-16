DAYS_PER_MONTH = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31    
}

DAYS = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    'Saturday', 'Sunday']

def build_empty_cal(month, first_day):
  months_cal = {}
  index = DAYS.index(first_day)
  start = month[:3]
  vl = None 
  for day in range(1, DAYS_PER_MONTH[month] + 1):
    key_string = '{}, {} {}'.format(str(DAYS[index % 7]),
    start, str(day))
    months_cal[key_string] = vl
    index += 1
  return months_cal
    


calendar = build_empty_cal('February', 'Thursday')
print(calendar)


# Warning,
expected = {
    "Thursday, Feb 1": None,
    "Friday, Feb 2": None,
    "Saturday, Feb 3": None,
    "Sunday, Feb 4": None,
    "Monday, Feb 5": None,
    "Tuesday, Feb 6": None,
    "Wednesday, Feb 7": None,
    "Thursday, Feb 8": None,
    "Friday, Feb 9": None,
    "Saturday, Feb 10": None,
    "Sunday, Feb 11": None,
    "Monday, Feb 12": None,
    "Tuesday, Feb 13": None,
    "Wednesday, Feb 14": None,
    "Thursday, Feb 15": None,
    "Friday, Feb 16": None,
    "Saturday, Feb 17": None,
    "Sunday, Feb 18": None,
    "Monday, Feb 19": None,
    "Tuesday, Feb 20": None,
    "Wednesday, Feb 21": None,
    "Thursday, Feb 22": None,
    "Friday, Feb 23": None,
    "Saturday, Feb 24": None,
    "Sunday, Feb 25": None,
    "Monday, Feb 26": None,
    "Tuesday, Feb 27": None,
    "Wednesday, Feb 28": None,
}

assert calendar == expected
print('all good')

def keys_for_each_day(cal, day):
  keys = []
  for key in cal.keys():
    if key.startswith(day):
      keys.append(key)
  return keys

def add_task(calendar, day_of_week, task):
  #Find All Days for day passed
  all_days = keys_for_each_day(calendar, day_of_week)
  #Loop through returned keys and add task as value for eack key
  for day in all_days:
    calendar[day] = task


add_task(calendar, 'Monday', 'Class')
add_task(calendar, 'Friday', 'Go Wild!')
print(calendar)

DAYS_PER_MONTH = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31    
}

def same_month_count(dictionary):
  count = {}
  for days in dictionary.values():
    count.setdefault(days, 0)
    count[days] += 1
  return count
print(same_month_count(DAYS_PER_MONTH))
