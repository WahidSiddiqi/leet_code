# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(nums.count(0))

for number in nums:
    while nums.count(number) != 1:
        nums.remove(number)
print(nums)