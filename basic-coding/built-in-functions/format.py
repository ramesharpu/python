def test():
    print "Printing '30' in binary format"
    print format(30, 'b')

    print "Using zfill"
    print format(30, 'b').zfill(8)

if __name__ == '__main__':
    test()