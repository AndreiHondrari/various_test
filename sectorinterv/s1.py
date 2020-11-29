"""
Suppose that you are part of a team that breaks electric locks. The way the team operates
is that there is a spy that overlooks what pin is introduced into the lock’s keyboard and
reports it to you. Unfortunately he is not completely sure that he saw the correct combination
and all adjacent (vertical and horizontal) keys of a key could be the correct key.

Given a keyboard and a reported pin, your task is to generate all possible variations of the observed pin. The pin can have any length.

Example:

Keyboard = [
	[1, 2, 3]
	[4, 5, 6]
	[7, 8, 9]
	[*, 0, #]
]

Reported_pin = “13”

Possible variations = [“13”, “23”, “43”, “12”, “22”, “42”, “16”, “26”, “46”]

Explanation:

Adjacent keys of 1 are 2 and 4 and adjacent keys of 3 are 2 and 6


"""

from collections import defaultdict
from copy import copy
from itertools import permutations

KEYBOARD = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	["*", 0, "#"],
]

collected_indexes = []
reported_pin = "19"

REPORTED_LEN = len(reported_pin)

nearing_symbols = defaultdict(set)

for stolen_symbol in reported_pin:
    MAX_ROWS = len(KEYBOARD)
    for i in range(MAX_ROWS):
        row = KEYBOARD[i]
        MAX_COLUMNS = len(row)

        for j in range(MAX_COLUMNS):
            if str(row[j]) == stolen_symbol:
                nearing_symbols[stolen_symbol].add(stolen_symbol)

                # get neighbours
                # x-1
                if (j-1) >= 0:
                    val = KEYBOARD[i][j-1]
                    nearing_symbols[stolen_symbol].add(str(val))

                # x+1
                if (j+1) < MAX_COLUMNS:
                    val = KEYBOARD[i][j+1]
                    nearing_symbols[stolen_symbol].add(str(val))

                # y-1
                if (i-1) >= 0:
                    val = KEYBOARD[i-1][j]
                    nearing_symbols[stolen_symbol].add(str(val))

                # y+1
                if (i+1) < MAX_ROWS:
                    val = KEYBOARD[i+1][j]
                    nearing_symbols[stolen_symbol].add(str(val))


resulting_combinations = []


def compute_combinations(reported_pin, resulting_combinations, nearing_symbols, partial_combo="", current_symbol_index=0):
    if current_symbol_index >= len(reported_pin):
        resulting_combinations.append(partial_combo)
        return

    stolen_symbol = reported_pin[current_symbol_index]
    combination = []
    for nearing in nearing_symbols[stolen_symbol]:
        compute_combinations(
            reported_pin,
            resulting_combinations,
            nearing_symbols,
            partial_combo+nearing,
            current_symbol_index+1
        )

compute_combinations(reported_pin, resulting_combinations, nearing_symbols)





print(resulting_combinations)
