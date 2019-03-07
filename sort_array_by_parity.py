class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_array = []
        odd_array = []
        for element in A:
            if element % 2 == 0:
                even_array.append(element)
            else:
                odd_array.append(element)
        final_array = even_array + odd_array
        return final_array