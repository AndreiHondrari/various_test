from collections import defaultdict


def transform_into_distinct_wordlist(wordlist):
    """Eliminate duplicates"""
    words_dict = dict()
    distinct_wordlist = []
    for word in wordlist:
        # no need in dealing with duplicates
        if word in words_dict:
            continue

        distinct_wordlist.append(word)
        words_dict[word] = 0

    return distinct_wordlist


def generate_groups_for_wordlist(indexed_wordlist):
    """
    Scan words to form starting, middle and ending sequences of characters
    of different scales 2 to max-1.
    """

    starting_groups = defaultdict(list)
    middle_groups = defaultdict(list)
    ending_groups = defaultdict(list)

    for index, word in indexed_wordlist.items():

        # scan word for groups
        for scale in range(1, len(word)):

            # starting
            start_group = word[:scale]
            starting_groups[start_group].append(index)

            # middle
            for offset in range(1, len(word) - scale):
                mid_group = word[offset:offset+scale]
                middle_groups[mid_group].append(index)

            # ending
            end_group = word[-scale:]
            ending_groups[end_group].append(index)

    return (
        starting_groups,
        middle_groups,
        ending_groups,
    )


def compute_degrees(groups):
    """
    Groups groups by degree (by length)
    """
    degree_pairs = defaultdict(set)

    for group, word_indexes in groups.items():
        degree = len(group)
        group_wi_pairs = [(group, wi) for wi in word_indexes]
        degree_pairs[degree] = degree_pairs[degree].union(group_wi_pairs)

    return degree_pairs


def combine_words(starting_word, ending_word, scale):
    """
    Combines two words in a dragging fashion:
       DEFGHI -> starting_word, the leading one
    ABCDEF -> ending_word, the dragging one
    """
    total_length = len(starting_word) + len(ending_word) - scale

    final_word = []
    for i in range(total_length):
        if i < len(ending_word):
            final_word.append(ending_word[i])
        else:
            final_word.append(starting_word[i - len(ending_word) + scale])

    return "".join(final_word)


def cross_combine(
    indexed_wordlist,
    starting_groups,
    starting_degree_pairs,
    middle_groups,
    ending_groups
):
    combination_pairs = dict()
    reverse_combination_track = dict()
    used_groupds = dict()
    unmatched = set()

    while len(starting_degree_pairs) > 0:
        # always pick the biggest
        max_degree = max(starting_degree_pairs.keys())

        for group_word_pair in starting_degree_pairs[max_degree]:
            current_word_group = group_word_pair[0]
            current_word_index = group_word_pair[1]

            current_word = indexed_wordlist[current_word_index]

            # check if the word is fully included in other
            if (
                current_word in starting_groups or
                current_word in middle_groups or
                current_word in ending_groups
            ):
                continue

            # if not included in other words then attempt to match it
            is_unmatched = True
            if (
                current_word_group in ending_groups and
                current_word_index not in combination_pairs and
                current_word_index not in reverse_combination_track
            ):
                # match found for ending -> attempt at combining it
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

        del starting_degree_pairs[max_degree]

    # post process endings
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

            print(f"ADD UNMAT {word_index} {current_word}")
            unmatched.add((word_index, current_word))

    # build the final list
    final_list = []
    unmatched_refined = []

    for x in unmatched:
        # if the word was already used drop it
        if x[0] in combination_pairs or x[0] in reverse_combination_track:
            continue

        final_list.append(x[1])

    for starting_word_index, ending_word_pair in combination_pairs.items():
        starting_word = indexed_wordlist[starting_word_index]
        ending_word = indexed_wordlist[ending_word_pair[0]]
        scale = ending_word_pair[1]

        final_list.append(combine_words(starting_word, ending_word, scale))

    combinations_exist = (len(combination_pairs) > 0)
    return final_list, combinations_exist


def cross_words(wordlist):
    indexed_wordlist = dict(enumerate(wordlist))

    # groups for wordlist
    (
        starting_groups,
        middle_groups,
        ending_groups,
    ) = generate_groups_for_wordlist(indexed_wordlist)

    # calculate scores based on groups
    # map degree -> list of groups for each degree (length)
    starting_degree_pairs = compute_degrees(starting_groups)

    print(starting_degree_pairs)

    new_wordlist, combinations_exist = cross_combine(
        indexed_wordlist,
        starting_groups,
        starting_degree_pairs,
        middle_groups,
        ending_groups
    )
    return new_wordlist, combinations_exist
