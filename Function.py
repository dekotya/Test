def maximum(A):
    max = A[0]
    for a in A:
        if a > max:
            max = a
    return max

A = [2, 4, 6, 4, 8, 9, 5]
max = maximum(A)
max

