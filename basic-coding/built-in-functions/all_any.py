# checks whether all/any item in teh list are True


def all_true(list):
    print "output of all function - {}".format(all(list))

def any_true(list):
    print "output of any function - {}".format(any(list))

def example():
    new_list = [True, True, True, False, True, True]
    print "List contains : "
    print new_list
    all_true(new_list)
    any_true(new_list)

if __name__ == '__main__':
    example()