from collections import defaultdict

from faker import Faker

from func1 import (
    transform_into_distinct_wordlist,
    generate_groups_for_wordlist,
)

fake = Faker()

wordlistX = [
    fake.pystr(min_chars=2, max_chars=5).upper()
    for _ in range(500)
]

wordlist1 = [
    "ABCD",
    "BCDE",
    "BCDF",
    "CDF",
]

wordlist2 = [
    "ABCD",
    # "CDE",
    # "KABC",
    # "DEZ",
    "MMM"
]



distinct_wordlist = transform_into_distinct_wordlist(wordlist2)

indexed_wordlist = dict(enumerate(distinct_wordlist))
(
    starting_groups,
    middle_groups,
    ending_groups,
    words_to_starting_groups,
    words_to_ending_groups
) = generate_groups_for_wordlist(indexed_wordlist)

print("\n---")
for i, x in indexed_wordlist.items():
    print(i, x)

# calculate scores based on groups
starting_degree_pairs = defaultdict(set)
ending_degree_pairs = defaultdict(set)
degree_pairs = defaultdict(list)

# map degree -> list of
for group, word_indexes in starting_groups.items():
    degree = len(group)
    group_wi_pairs = [(group, wi) for wi in word_indexes]
    starting_degree_pairs[degree] = starting_degree_pairs[degree].union(group_wi_pairs)

# for group, word_indexes in ending_groups.items():
#     degree = len(group)
#     group_wi_pairs = [(group, wi) for wi in word_indexes]
#     ending_degree_pairs[degree] = ending_degree_pairs[degree].union(group_wi_pairs)

print("\n---")
for x, y in starting_degree_pairs.items():
    print(f"{x} {y}")

# print("\n---")
# for x, y in ending_degree_pairs.items():
#     print(f"{x} {y}")

print("\n---")


combination_pairs = dict()
reverse_combination_track = dict()
used_groupds = dict()
unmatched = set()

while len(starting_degree_pairs) > 0:
    # always pick the biggest
    max_degree = max(starting_degree_pairs.keys())
    print(f"\nSTA DEG {max_degree}")

    for group_word_pair in starting_degree_pairs[max_degree]:
        print(f"WI {group_word_pair}")

        current_word_group = group_word_pair[0]
        current_word_index = group_word_pair[1]

        current_word = indexed_wordlist[current_word_index]

        # check if the word is fully included in other
        if (
            current_word in starting_groups or
            current_word in middle_groups or
            current_word in ending_groups
        ):
            print(f"Included, skip {current_word}")
            continue

        # if not included in other words then attempt to match it
        is_unmatched = True
        if (
            current_word_group in ending_groups and
            current_word_index not in combination_pairs and
            current_word_index not in reverse_combination_track
        ):
            # match found for ending -> attempt at combining it
            print('-> matched')

            while len(ending_groups[current_word_group]) > 0:
                # fetch an word ending with this group
                other_word_index = ending_groups[current_word_group].pop(0)

                if current_word_index == other_word_index:
                    continue

                if (
                    other_word_index not in combination_pairs and
                    other_word_index not in reverse_combination_track
                ):

                    combination_pairs[current_word_index] = (
                        other_word_index, max_degree,
                    )
                    reverse_combination_track[other_word_index] = current_word_index
                    is_unmatched = False
                    break  # no need to attempt with another word from the ending set

            # if the processing resulted in depletion of the specific set
            # for an ending group, no need to keep it there anymore
            if len(ending_groups[current_word_group]) == 0:
                del ending_groups[current_word_group]

        if is_unmatched:
            unmatched.add((current_word_index, current_word))
            print("-> not matched")

    del starting_degree_pairs[max_degree]

# post process endings
print("\n--- ENDINGS POST PROCESSING")
# for end_group, end_group_words_indexes in ending_groups.items():
while len(ending_groups) > 0:
    end_group, end_group_words_indexes = ending_groups.popitem()
    for word_index in end_group_words_indexes:
        current_word = indexed_wordlist[word_index]

        if (
            current_word in starting_groups or
            current_word in middle_groups or
            current_word in ending_groups
        ):
            continue

        unmatched.add((word_index, current_word))

print("\n--- UNMATCHED POST PROCESSING")
unmatched_refined = []
for x in unmatched:
    # if the word was already used drop it
    if x[0] in combination_pairs or x[0] in reverse_combination_track:
        print(f"{x} already used")
        continue

    print(f"{x} is lonely")
    unmatched_refined.append(x)

print("\n--- UNMATCHED")
for x in unmatched_refined:
    print(f"{x}")

print("\n--- ENDINGS LEFT")
for x, y in ending_groups.items():
    print(f"{x}, {y}")

print("\n--- COMBINATIONS")
for combo, pair in combination_pairs.items():
    print(f"({combo}, {pair[0]}): {pair[1]}")

print("\n---")
print("DONE")
