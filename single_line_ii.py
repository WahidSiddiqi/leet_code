# def singleNumber(nums):
#     nums.sort()
#     while nums[0] == nums[2]:
#         del nums[0:3]
#         if len(nums) == 1 or nums[0] != nums[2]:
#             break
#     return nums[0]
#
# singleNumber([2, 2, 3, 2])

nums1 = [2, 2, 3, 2]
def unique(nums):

    while len(nums) > 1:
        nums[0] == nums[2]
        del nums[0:3]

    print(nums[0])

unique(nums1)