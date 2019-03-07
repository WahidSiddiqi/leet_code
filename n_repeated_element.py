def repeatedNTimes(A):
    b = A[0]
    A.pop(0)
    while b not in A:
        b = A[0]
        A.pop(0)
    print(b)

