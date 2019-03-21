class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = dict.fromkeys(nums, 0)
        for number in nums:
            nums_dict[number] += 1
        for key, value in nums_dict.items():
            if value >= 2:
                return key