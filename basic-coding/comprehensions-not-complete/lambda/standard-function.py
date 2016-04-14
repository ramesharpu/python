#!/usr/bin/python

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print "foo", foo

print "Filter: (is it divisible by 3"
print filter(lambda x: x % 3 == 0, foo)

print "Map: x * 2 + 10"
print map(lambda x: x * 2 + 10, foo)

print "Reduce: sum of the foo value"
print reduce(lambda x, y: x + y, foo)
