
class E1(Exception):
    pass

class E2(Exception):
    pass

class E3(Exception):
    pass


try:
    raise E2("este")
except (E1, E2) as e:
    print("AAAAA")
    print(e.strerror)

print("EEEE")
