class A():
    foo = 1

class B(A):
    pass

if __name__ == '__main__':
    b = B()
    print hasattr(b, 'foo')
    print 'foo' in b.__dict__
