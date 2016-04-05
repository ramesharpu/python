# iterators is explained using for loop

def test():
    print "Printing the numbers in defined list: "
    for i in [1, 2, 3, 4, 5]:
        print i


def test1():
    print "Printing character of 'python':"
    for c in "python":
        print c

def test2():
    dict = {"x": 1, "y": 2}
    print "Printing dictionary keys"
    for k in dict:
        print k

    print "Printing dictionary values"
    for k, l in dict.items():
        print l
    print "another approach"
    for k in dict.values():
        print k

    print "Printing the dictionary key:value pair"
    for k in dict.items():
        print k


def test3():
    x = iter([1, 2, 3])
    print x
    print x.next()
    print x.next()

if __name__ == '__main__':
    test()
    test1()
    test2()
    test3()