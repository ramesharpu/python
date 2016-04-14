class A():
    x = 10
    print "### Global output from class A"
    print globals()

class B(A):
    y = A.x
    x = 20
    print "### Global output from class B"
    print globals()
    print "### Local output from class B"
    print locals()
