class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if row > 0 and column > 0 and matrix[row][column] != matrix[row - 1][column - 1]:
                    return False
        return True