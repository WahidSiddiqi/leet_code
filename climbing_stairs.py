def climbStairs(n):
    if n == 1:
        return n
    if n == 0:
        return 0
    return climbStairs(n - 1) + climbStairs(n - 2)

print(climbStairs(20))