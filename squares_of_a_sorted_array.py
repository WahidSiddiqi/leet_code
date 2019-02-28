def negIntoPositive(aNumber):
    return abs(aNumber)

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        positive_list = []
        for number in A:
            positive_list.append(abs(number*number))
        positive_list.sort()
        return positive_list