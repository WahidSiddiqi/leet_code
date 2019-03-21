class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum_of_nums = 0
        nums.sort()
        for number in range(0, len(nums), 2):
            sum_of_nums += nums[number]
        return sum_of_nums