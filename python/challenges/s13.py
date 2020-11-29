def solution(A, K):
    try:
        remainder = K % len(A)
    except ZeroDivisionError:
        return A

    si = remainder
    return A[-si:] + A[:-si]

l1 = [11, 22, 33, 44]
l2 = [5, -1000]

print(solution(l1, 0))
print(solution(l1, 3))
print(solution(l1, 4))
print(solution(l1, 6))

print(solution(l2, 1))
