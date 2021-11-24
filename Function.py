def minimum(A):
    min = A[0]
    for a in A:
        if a < min:
            min = a
    return min

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
min = minimum(A)
min

