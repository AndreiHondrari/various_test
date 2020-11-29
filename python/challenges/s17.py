def solution(A):
    """
    Check if array is permutation
    """

    A = sorted(A)

    if len(A) == 0:
        return 1

    is_first_correct = (A[0] == 1)

    if not is_first_correct:
        return 0
    elif len(A) == 1:
        return 1

    for i in range(len(A)):
        curr_item = A[i]

        try:
            next_item = A[i+1]
        except IndexError:
            break

        if curr_item + 1 != next_item:
            return 0

    return 1
