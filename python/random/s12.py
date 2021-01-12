

class A:
    pass


class B(A):
    pass

class C(B):
    pass

class D(A):
    pass

x = A.__subclasses__()

print(x)

print(B.__qualname__)
