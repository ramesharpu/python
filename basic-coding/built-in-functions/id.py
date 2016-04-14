"""
Return the 'identity' of an object.
This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime.
Two objects with non-overlapping lifetimes may have the same id() value.

CPython implementation detail: This is the address of the object in memory.
"""

foo = 1
bar = foo
test_bar = bar
test = 1

# All of the below will return the same value as the memory location is the same
print id(foo)
print id(bar)
print id(test_bar)
print id(test)
