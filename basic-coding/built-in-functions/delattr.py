class Test():
    y = 20
    def __init__(self):
        self.x = 10

def objectclass():
    cda = Test()
    # this will print the value
    print "The value of x is {}".format(cda.x)
    # after deleting the attribute value,  it throws stacktrace
    delattr(cda, "x")
    print "The value of x is {}".format(cda.x)


    def readonly():
        abc = Test()
        print "The value of y is {}".format(cda.y)
        # while deleting the attribute value,  it throws stacktrace
        delattr(abc, "x")
        print "The value of x is {}".format(cda.y)


if __name__ == '__main__':
    '''Uncomment each method and keep the other methods as is to see their output'''
    uobjectclass()
    # readonly()