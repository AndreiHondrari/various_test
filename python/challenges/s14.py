def solution(A):
    if len(A) == 0:
        return 1

    if len(A) == 1 and A[0] == 1:
        return 2

    A = sorted(A)

    if A[0] != 1:
        return 1

    last = None
    for i in range(1, len(A)):
        prev = A[i-1]
        curr = A[i]
        last = curr

        expected = prev + 1
        if expected != curr:
            return expected

    return last + 1

print(solution([]))  # 1
print(solution([1,]))  # 2
print(solution([2,]))  # 1
print(solution([1, 2]))  # 3
print(solution([1, 3]))  # 2
print(solution([2, 3]))  # 1
print(solution([2, 3, 1, 5]))  # 4
