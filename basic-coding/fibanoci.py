"""Print the first ten values of the fibanacci series"""
def fibonacci(n, first=0, second=1):
    print "General method"
    while n != 0:
        print(first)
        n, first, second = n - 1, second, first + second
fibonacci(10)


"""using yield"""
def fibonacci_yield(n, first=0, second=1):
    print "\nUsing yield"
    while n != 0:
        yield first
        n, first, second = n - 1, second, first + second
print(list(fibonacci_yield(10)))
