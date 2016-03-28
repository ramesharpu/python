##Yield example

def yield_example(n):
    for i in range(n):
        yield i
        print "End of the method"

# method 1 to get the results
print (list(yield_example(10)))

# method 2 to get the results in an iterative way
test = yield_example(3)
print test.next() # Call this 3 times to print the value
