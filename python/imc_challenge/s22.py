
# sw1 = 0 if i < len(w2) else (i+1) - len(w2)
# ew1 = len(w1) if (i+1) >= len(w1) else i + 1
# sw2 = 0 if len(w2) < (i+1) else len(w2) - i - 1
# ew2 = len(w2)


def max_intersection_score_for_words(w1, w2):
    print(f"LEN w1: {w1} {len(w1)}")
    print(f"LEN w2: {w2} {len(w2)}")

    final_offset = len(w2) + len(w1) - 1
    max_score = 0
    max_at_offset = None
    for offset in range(final_offset):

        # calculate score for current offset (i)
        current_score = 0
        w2i_offset = len(w2) - 1 - offset
        difference_encountered = False
        for j in range(len(w1)):
            w2i = w2i_offset + j
            if w2i >= 0 and w2i < len(w2):
                w1c = w1[j]
                w2c = w2[w2i]
                res = (w1c == w2c)
                # print(f"{offset} {j} {w1c} {w2c} {res}")

                if res:
                    current_score += 1
                else:
                    difference_encountered = True
                    break


        if not difference_encountered and current_score > max_score:
            max_score = current_score
            max_at_offset = offset

    return max_score, max_at_offset

def combine_words(w1, w2, w2_offset):
    for i in range(len(w1) + len(w2) - 1 - w2_offset):
        print(i)


# a = "MMM"
a = "BAXC"
b = "XAB"
s1, o1 = max_intersection_score_for_words(a, b)
c1 = None
if s1 != 0:
    c1 = combine_words(a, b, o1)
print(f"{s1} {o1} {c1}\n")

s2, o2 = max_intersection_score_for_words(b, a)
c2 = None
if s2 != 0:
    c2 = combine_words(b, a, o2)
print(f"{s2} {o2} {c2}\n")
