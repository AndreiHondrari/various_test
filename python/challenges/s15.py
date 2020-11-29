from datetime import datetime

def solution(X, A):

    position = 0

    unhopped_positions = {}
    for i in range(1, X + 1):
        unhopped_positions[i] = False

    for i in range(len(A)):
        p = A[i]

        if not unhopped_positions[p]:
            unhopped_positions[p] = True

            for j in range(position + 1, X + 1):
                if unhopped_positions[j]:
                    position += 1
                else:
                    break

        if position >= X:
            return i

    return -1


l1 = range(1, 9998)
l1 = list(l1[::-1])
print(datetime.now())
print(solution(9999, l1 + [9999]))
print(datetime.now())
