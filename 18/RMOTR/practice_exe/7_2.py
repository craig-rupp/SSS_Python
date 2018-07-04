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