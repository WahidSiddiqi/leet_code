class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_arr = []
        even_arr = []
        sorted = []
        for number in A:
            if number % 2 == 0:
                even_arr.append(number)
            else:
                odd_arr.append(number)
        for i in range(len(odd_arr)):
            sorted.append(even_arr[i])
            sorted.append(odd_arr[i])
        return sorted