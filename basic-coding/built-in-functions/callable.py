"""
with attribute __call__, the object becomes callable
which means we can call the class __init__ method using class(). when class() is used, def __call__() is called.
"""

class Add():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print "Sum of {} and {} is {}".format(self.num1, self.num2, self.num1+self.num2)

    def __call__(self):
        return (self.num1+self.num2)

# This calls the class __init__ method
add = Add(1,2)

# This calls the __call__ method.
# If no __call__ method is defined then we get error stating "AttributeError: Add instance has no __call__ method"
print add()