class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for number in nums:
            if number == 0:
                nums.append(number)
                nums.remove(number)