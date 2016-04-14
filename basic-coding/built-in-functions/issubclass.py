class A():
    pass

class B(A):
    pass

class C():
    pass

b = B()
print issubclass(B, A)
print issubclass(B, C)
print issubclass(A, A)
print issubclass(B, (A, C))
