class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_change = []
        column_change = []
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    row_change.append(row)
                    column_change.append(column)
                    
        for i, val in enumerate(row_change):
            for j in range(len(matrix[0])):
                matrix[val][j] = 0
                
        for i, val in enumerate(column_change):
            for j in range(len(matrix)):
                matrix[j][val] = 0
                    
