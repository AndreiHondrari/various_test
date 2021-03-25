
from typing import overload, Union, Any


@overload
def do(x: int) -> str: ...


@overload
def do(x: list[Any]) -> float: ...


def do(x: Union[int, list[Any]]) -> Union[str, float]:
    if isinstance(x, int):
        return "bla"

    if isinstance(x, list):
        return 5.152
