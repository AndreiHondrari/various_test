def solution(A, B, K):

    div_count = 0

    n = A
    while n <= B:

        if n % K == 0:
            div_count += 1

        n += 1

    return div_count
