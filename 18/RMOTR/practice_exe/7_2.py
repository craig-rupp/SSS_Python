# Define your class here!
# Create a class TempConverter that has two optional parameters celsius and fahrenheit. When an object is created, if it receives neither of the optional parameters, raise a custom exception NoTemperatureException that you will need to create.

# You'll need to differentiate which type of temperature you receive when you create your object. If the object receives a Celsius temp, store it in a variable temp_celsius. If it receives a Fahrenheit temp, store it in a variable temp_fahrenheit.

# You need two methods: 
# to_celsius that returns the temperature in Celsius. If a Celsius input was received when the object was created, return that. Otherwise return the conversion formula (temp_fahrenheit - 32) * 5/9

# to_fahrenheit that returns the temperature in Fahrenheit. If a Fahrenheit input was received when the object was created, return that. Otherwise return the conversion formula (temp_celsius * 9/5) + 32

# Look up how to use the round() function on your answers to make them only have one decimal place to the right.
class NoTemperatureException(Exception):
    pass

class TempConverter(object):
    def __init__(self, celsius=None, fahrenheit=None):
        if not celsius and not fahrenheit:
            raise NoTemperatureException('Provide one weirdo')
        self.temp_celsius = celsius
        self.temp_fahrenheit = fahrenheit
        
    def to_celsius(self):
        if self.temp_celsius:
            return round(self.temp_celsius, 1)
        return round(((self.temp_fahrenheit - 32) * 5/9), 1)
            
    def to_fahrenheit(self):
        if self.temp_fahrenheit:
            return round(self.temp_fahrenheit, 1)
        return round(self.temp_celsius * 9/5 + 32, 1)

# Define Point class here
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define Line class here
class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2 
        
    def slope(self):
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
    
    def y_intercept(self):
        slp = self.slope()
        return self.p1.y - (slp * self.p1.x)
        
    def formula(self):
        rt_str = 'y = {m}x + {b:g}'
        m = self.slope()
        if m == 1:
            m = ''
        return rt_str.format(m=m, b=self.y_intercept())
    
p1 = Point(0, 1)
p2 = Point(1, 2)
l = Line(p1, p2)
print(l.slope())
print(l.y_intercept())
print(l.formula())

class Calculator(object):
    def __init__(self):
        self.cache = {}
        
    def add(self, a, b):
        self.a = a 
        self.b = b
        add_key = self.cache.setdefault('add', [])
        add_tup = (self.a, self.b, self.a + self.b)
        if add_tup not in add_key:
            add_key.append(add_tup)
            return add_tup[-1]
        search_list = self.cache['add']
        pull_tupe = search_list.index(add_tup)
        return search_list[pull_tupe][-1]
        
    def subtract(self, x, y):
        self.x = x 
        self.y = y 
        sub_key = self.cache.setdefault('subtract', [])
        sub_tup = (self.x, self.y, self.x - self.y)
        if sub_tup not in sub_key:
            sub_key.append(sub_tup)
            return sub_tup[-1]
        sub_search = self.cache['subtract']
        pull_sub_tupe = sub_search.index(sub_tup)
        return sub_search[pull_sub_tupe][-1]
        
        
c = Calculator()
print(c.cache)
print(c.add(2, 3))
print(c.add(2, 3))