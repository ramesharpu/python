""" https://docs.python.org/2/library/stdtypes.html#typesmapping """

''' There are various ways of declaring a dictionary'''

# first way
a = {'one': 1, 'two': 2, 'three': 3}
b = dict(one=1, two=2, three=3)
c = dict(zip(['one', 'two', 'three'],[1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

if __name__ == '__main__':
    print a == b == c == d == e