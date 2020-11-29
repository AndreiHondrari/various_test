
import enum

@enum.unique
class SomeBla(enum.Enum):
    X = "bla"
    Y = "foo"


print(SomeBla.X.value)
