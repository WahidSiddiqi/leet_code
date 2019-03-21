class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        single_numbers = []
        dict_list = dict.fromkeys(nums, 0)
        for number in nums:
            dict_list[number] += 1
        for number, count in dict_list.items():
            if count == 1:
                single_numbers.append(number)
        return single_numbers