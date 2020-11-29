

import json
from enum import Enum
from dataclasses import dataclass, asdict
import datetime

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value

        if isinstance(obj, datetime.datetime):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)

class SomeEnum(Enum):
    A = "fawfa"
    B = "qwtwq"


@dataclass
class X:
    sen: SomeEnum
    bla: str
    meh: datetime.datetime


x1 = X(sen=SomeEnum.B, bla="zzeeeett", meh=datetime.datetime.now())


print(SomeEnum.B)
print()
print(json.dumps(asdict(x1), cls=EnumEncoder))
