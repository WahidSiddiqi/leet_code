class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for arr in A:
            arr.reverse()
            for numb in range(len(A[0])):
                if arr[numb] == 0:
                    arr[numb] = 1
                elif arr[numb] == 1:
                    arr[numb] = 0
        return A