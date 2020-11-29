
import random
from collections import namedtuple

Item = namedtuple("Item", ["id", "weight", "value"])

MAX_ALLOWED = 5

class GetID:

    def __init__(self):
        self.current_id = 0

    def __call__(self):
        self.current_id += 1
        return self.current_id


get_id = GetID()

# define the collection of items
items_list = [
    Item(id=get_id(), weight=1, value=1000),
    Item(id=get_id(), weight=100, value=1),
]

for i in range(20):
    items_list.append(
        Item(
            id=get_id(),
            weight=random.randint(50, 100),
            value=random.randint(50, 100),
        )
    )


items_list += [
    Item(id=get_id(), weight=100, value=500),
    Item(id=get_id(), weight=50, value=500),
]

# print initial set
for i in items_list:
    print(i)

# sweep items and pick the winners
