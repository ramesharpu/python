"""
A @classmethod when we want to change the behaviour of the method based on which subclass is calling the method.
Note: we should have a reference to the calling class in a class method.
While using static you would want the behaviour to remain unchanged across subclasses
"""

class a():
    # Static method
    @staticmethod
    def say_hell0():
        print ("Static method to say Hello")

    @classmethod
    def say_class_hello(cls):
        if(cls.__name__=="b"):
            print ("Hello from class b")
        elif(cls.__name__=="c"):
            print ("Hello from class c")

class b(a):
    def hello(self):
        print "Test from class b"

class c(a):
    def hello(self):
        print "Test from class c"


if __name__ == '__main__':
    test1 = b()
    test1.say_class_hello()
    test1.say_hell0()
    test1.hello()

    test2 = c()
    test2.say_class_hello()
    test2.say_hell0()
    test2.hello()