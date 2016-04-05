def test():
    for i in range(10):
        yield i

def abc():
    new_list = list(test())
    for i in range(len(new_list)):
        print i
        print "test value for this is {}".format(i)

if __name__ == '__main__':
    abc()