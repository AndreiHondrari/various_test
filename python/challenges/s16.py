def solution(N, A):

    counters = dict()

    for i in range(N):
        counters[i] = 0

    max_cnt = 0
    floating_line = 0

    for i in range(len(A)):
        op = A[i]
        ci = op - 1
        if op <= N:
            counters[ci] = (counters[ci] + 1) if (counters[ci] >= floating_line) else (floating_line + 1)
            max_cnt = max(counters[ci], max_cnt)
        elif op == (N + 1):
            floating_line = max_cnt


    resulting = []
    for _, val in counters.items():
        val = (val if val >= floating_line else floating_line)
        resulting.append(val)

    return resulting
