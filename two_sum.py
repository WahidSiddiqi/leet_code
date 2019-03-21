def twoSum(nums, target):
    #Creates an empty dictionary
    dicts = {}
    #A for loop that loops 0 to the length of the list, nums
    for i in range(0, len(nums)):
        #Sets the variable 'x'  to nums[i]
        x = nums[i]
        #If x is in dicts
        if x in dicts:
            print([dicts.get(x), i])
        dicts[target - x] = i
        print(dicts)

twoSum([2, 5, 8, 11, 16], 13)

#
# x = 1   #nums[0] = 1
# if x in dicts: #dicts is empty, so it doesn't execute
#     print([dicts.get(x), i])
# dicts[18-1] = 17
#
# dicts[17]
#
# x = 2
#
# if x in dicts:
#     not true
# dicts[18-2] =
#
