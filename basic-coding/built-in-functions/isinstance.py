class A():
    pass

class B(A):
    pass

b = B()
print isinstance(b, A)
print isinstance(B, A)
print isinstance(B(), A)