import functools



def dec(func=None, *, something=None):

    def _inner_decorator(decorated_func):

        @functools.wraps(decorated_func)
        def _wrapper(*args, **kwargs):
            print(f"BEF {decorated_func}")
            decorated_func(*args, **kwargs)
            print(f"AFT {decorated_func}")

        return _wrapper

    if func is None:
        return _inner_decorator

    return _inner_decorator(func)


@dec
def myf(x, bla=None):
    print(f"DOING MYF {x} {bla}")


@dec()
def myf2(x, bla=None):
    print(f"DOING MYF2 {x} {bla}")


@dec(something=123456)
def myf3(x, bla=None):
    print(f"DOING MYF3 {x} {bla}")



myf(11, bla="abacus")
myf2(22, bla="potato")
myf3(33, bla="potataxxx")
