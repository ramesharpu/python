#!/usr/bin/python


def increment(value):
    return lambda x: x + value

f = increment(2)
print "By defining a variable to call the function i.e, f(24): ", f(24)
print "Directly calling the increment function eg. increment(25)(25):", increment(25)(25)
