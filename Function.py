def maximum(A):
    max = A[0]
    for a in A:
        if a > max:
            max = a
    return max

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
max = maximum(A)
max

