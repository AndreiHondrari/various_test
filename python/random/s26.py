

def f1():

    x = 10

    def f2():
        return x

    return f2

print(f1()())
