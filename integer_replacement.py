def integerReplacement(n):
    print(n)
    while n is not 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        if n % 2 != 0:
            n = n - 1
            print(n)
    return n