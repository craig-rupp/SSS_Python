class Commercial(object):
    def __init__(self, dicto):
        for key, value in dicto.items():
            setattr(self, key, value)

tide_ad = Commercial({
                    "actor": "David Harbour",
                    "brand": "Tide",
                    "style": "Really weird",
                    "warning": "Don't eat Tide Pods"
})
print(tide_ad.actor)

class Location(object):
    def __init__(self, dicto):
        for key, value in dicto.items():
            setattr(self, key.lower(), value.lower())
    
    #@classmethod
    def search(self, list_o_guesses):
        prizes = []
        for guess in list_o_guesses:
            print(guess)
            if hasattr(self, guess):
                prizes.append(getattr(self, guess.lower()))
        return prizes
        
house = Location({
    'dresser': 'socks',
    'pantry': 'cake',
    'safe': 'money'
})
print(house.search(['basement', 'closet', 'dresser']))

########################
# These are already implemented. No need to change them:
class Loan(object):
    def __init__(self, value):
        self.value = value

class Movie(object):
    def __init__(self, price):
        self.price = price

class Milk(object):
    def __init__(self, cost):
        self.cost = cost
########################

# Your task:
def calculate(p1, p2):
    total = 0
    df_vals = ['value', 'price', 'cost']
    for obj in [p1, p2]:
        for val in df_vals:
            if hasattr(obj, val):
                total += getattr(obj, val)
    return total

