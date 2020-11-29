def solution(xs):
    assert 1 <= len(xs) <= 50

    # product is between two numbers, so return only one
    if len(xs) == 1:
        return str(xs[0])

    xs = sorted(xs)

    max_output = 0
    previous_negative = None

    all_n_null = True
    for n in xs:
        assert abs(n) <= 1000

        if n == 0:
            # discard zero values
            continue
        else:
            # detect non-zero value
            all_n_null = False

        # handle negatives
        if n < 0:
            if previous_negative is None:
                previous_negative = n
            else:
                if max_output == 0:
                    max_output = 1
                max_output *= (n * previous_negative)
                previous_negative = None

            continue

        # handle positives
        if max_output == 0:
            max_output = 1
        max_output *= n

    if all_n_null:
        return str(0)

    return str(max_output)
