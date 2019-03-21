class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        elif n < 1:
            return False
        while n > 1:
            if n == 2:
                return True
            elif n % 2 != 0:
                return False
            n = n / 2