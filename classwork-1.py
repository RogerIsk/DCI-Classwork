'''
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    def __add__(self, other):
        return Pizza(self.toppings + other.toppings)
    
    def __add__(self, other):
        if isinstance(other, Pizza):
            combined_toppings = self.toppings + other.toppings
            return Pizza(self.toppings + other.toppings)
        else:
            raise TypeError("You can only add two pizzas together")



pizza1 = Pizza(["cheese", "pepperoni"])
pizza2 = Pizza(["cheese", "mushrooms"])

print(pizza1.toppings)
print(pizza2.toppings)

pizza3 = pizza1 + pizza2
dir(pizza1)
'''


class MyClass:
    def __mymagic__(self):
        return "magic method called"
    
def __mymagic__(obj):
    if hasattr(obj, "__mymagic__"):
        return obj.__mymagic__()
    else:
        raise TimeoutError("No magic method found")
    
obj = MyClass()
some_obj = list()

print(__mymagic__(obj))
print(__mymagic__(some_obj))