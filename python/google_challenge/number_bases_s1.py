
def int_to_base(n, new_base):

    if new_base == 10:
        return n

    final_number = []
    quotient = n

    while True:
        quotient = n // new_base
        remainder = n % new_base
        n = quotient
        final_number.append(str(remainder))

        if quotient <= 0:
            break

    return "".join(final_number[::-1])

def next_n(n, b, k):
    output_format = "{{:0>{}}}".format(k)
    x = sorted(n, reverse=True)
    y = sorted(n)

    int_x = int("".join(x), base=b)
    int_y = int("".join(y), base=b)
    int_z = int_x - int_y
    new_n = int_to_base(int_z, b)
    return output_format.format(new_n)


def solution(n, b):
    k = len(n)
    assert 2 <= k <= 9
    assert 2 <= b <= 10

    loop_size = 1
    numbers_tracker = dict()
    loop_starting_number = None

    while True:
        n = next_n(n, b, k)

        if n in numbers_tracker:

            # mark the starting of the loop
            if loop_starting_number is None:
                loop_starting_number = n

            # detect the end of the loop
            elif loop_starting_number == n:
                break

            # count the numbers in the middle of the loop
            else:
                loop_size += 1
        else:
            numbers_tracker[n] = None

    return loop_size

if __name__ == "__main__":
    n = '210022'
    base = 3

    res = solution(n, base)
    print "\n--- RES {}".format(res)
