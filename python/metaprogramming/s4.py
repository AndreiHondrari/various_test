


class Metaclass1(type):

    # def __prepare__(name, bases, *args, **kwargs):
    #     print(f"Metaclass1.__prepare__ name: {name}")
    #     print(f"Metaclass1.__prepare__ bases: {bases}")
    #     print(f"Metaclass1.__prepare__ args: {args}")
    #     print(f"Metaclass1.__prepare__ kwargs: {kwargs}")
    #     return {
    #         'prepare_named_arg': 333
    #     }

    def __new__(cls, name, bases, namespace, *args, **kwargs):
        return super().__new__(cls, name, bases, namespace, *args)

    def __init__(self, name, bases, namespace, *args, **kwargs):
        print(f"\n\nMetaclass1.__init__ self: {self}")
        print(f"Metaclass1.__init__ bases: {bases}")
        print(f"Metaclass1.__init__ namespace: {namespace}")
        print(f"Metaclass1.__init__ args: {args}")
        print(f"Metaclass1.__init__ kwargs: {kwargs}")

        print(self.mro())


class Meta1(type):

    def __init__(self, name, bases, namespace, *args, **kwargs):
        print(f"\n{self}")
        print(f"Meta1.__init__ kwargs: {kwargs}")


class A:

    def __init_subclass__(klass, *args, **kwargs):
        if A in klass.__bases__:
            print(f"JACKPOT! {klass}")

class D:
    pass

class B(A, D):
    pass


class C(B, f=1234):
    pass

class X(A):
    pass
