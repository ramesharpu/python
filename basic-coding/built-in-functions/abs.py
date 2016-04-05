"""

# Returns the absolute value of a number
Arguments:
    plain or long integer
    floating point number
PS: if complex number then its magnitude will be returned
"""

def absexample(value):
    print "Absolute value of {} is {}\n".format(value, abs(value))

def integer_example():
    print "# Integer value"
    absexample(-5)

def longinteger_example():
    print "# Long interger value"
    absexample(-281473648)

def complex_example():
    print "#Complex number"
    x = complex(-4, 2)
    absexample(x)

if __name__ == '__main__':
    integer_example()
    longinteger_example()
    complex_example()