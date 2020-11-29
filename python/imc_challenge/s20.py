"""
------------------------------

World Index Problem

------------------------------
"""

from collections import defaultdict, namedtuple
from faker import Faker

fake = Faker()

ScoreTuple = namedtuple(
    'ScoreTuple',
    [
        'current_letter_index',
        'cross_result_index',
        'edge_index'
        'overflows',
        'overflows_beginning'
    ]
)

print("Fun stuff\n------------------------------\n")

world_index_names = [
    "NVDA",
    "XNV",
    "DAX"
]

# final list
total_length = 0
result = []

# keeps a track of the existing letter positions in the result
# letter -> index -> last total length
letter_indexes = defaultdict(dict)


for index_name in world_index_names:

    # score -> list of ScoreTuple's
    cross_scores = defaultdict(list)

    index_name_letters = list(index_name)

    # initialization if empty
    if len(result) == 0:
        # put the first index name in the result
        result = index_name_letters

        # evaluate the total length of the result
        total_length = len(result)

        # register the positions in the result of the letters
        for letter_i, letter in enumerate(result):
            letter_indexes[letter][letter_i] = total_length

    # time to identify the crossings
    for letter_i, letter in enumerate(index_name_letters):
        # get existing indexes
        existing_result_positions = []

        # index -> last total length
        letter_positions = letter_indexes[letter]

        # check crossing
        for i in range(len(index_name_letters)):
             
