class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        max_number = (max(A)-K)
        min_number = (min(A)+K)
        if len(A) < 2:
            return 0
        return max((max_number-min_number),0)