import random
import string

from faker import Faker

from func1 import (
    transform_into_distinct_wordlist,
    cross_words,
)

fake = Faker()

wordlistX = [
    fake.pystr(min_chars=2, max_chars=5).upper()
    for _ in range(500)
]

wordlistY = [
    'AAAA'
    for _ in range(50)
]

wordlistY += [
    'BBBB'
    for _ in range(50)
]

wordlistZ = [
    "".join([random.sample([c for c in "AB"], k=1)[0] for _ in range(5)])
    for _ in range(100)
]

wordlistZZ = [
    c * 5
    for c in string.ascii_uppercase
]

wordlist1 = [
    "ABCD",
    "BCDE",
    "BCDF",
    "CDF",
]

wordlist2 = [
    "ABCD",
    "CDE",
    "KABC",
    "DEZ",
    "MMM"
]

wordlist3 = [
    "XNV",
    "NVDA",
    "DAX",
]

input_wordlist = wordlist3

wordlist = transform_into_distinct_wordlist(input_wordlist)

combinations_exist = True
while combinations_exist:
    wordlist, combinations_exist = cross_words(wordlist)
    print(f"Combinations exist: {combinations_exist}")
    for x in wordlist:
        print(f"{x}")

final_result = "".join(wordlist)

print("\n ---- NOT FOUND")
total_length = 0
for x in input_wordlist:
    total_length += len(x)
    if x not in final_result:
        print(f"{x}")

print(f"\n --- FINAL: {final_result}")

print("\n --- SCORE")
S = total_length
L = len(final_result)
score = max(0, (S-L)/S)
print(f"TOTAL OF ALL {S}")
print(f"TOTAL OF ANS {L}")
print(f"SCORE {score}")

print("\n---")
print("DONE")
