"""
Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure.
If x is false or omitted, this returns False; otherwise it returns True.
bool is also a class, which is a subclass of int.
Class bool cannot be subclassed further. Its only instances are False and True
"""

def test():
    a = True
    print bool(a)

    b = None
    print bool(b)

    print bool(1)
    print bool(0)
    

if __name__ == '__main__':
    test()