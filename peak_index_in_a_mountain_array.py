class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        mountain_peak = max(A)
        return A.index(mountain_peak)