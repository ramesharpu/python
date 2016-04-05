"""
Compare the two objects x and y and return an integer according to the outcome.
The return value is negative if x < y, zero if x == y and strictly positive if x > y.
"""
def cmptest(a, b):
    print cmp(a,b)

if __name__ == '__main__':
    cmptest(4, 5)