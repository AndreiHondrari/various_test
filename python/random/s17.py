
import functools as ftools


@ftools.singledispatch
def do(arg: str) -> None:
    print(arg)


@do.register
def _(arg: int) -> int:
    return arg * 2


y1 = do("fwaf")
y2 = do(11)
print(f"{y1} {y2}")
