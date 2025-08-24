from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = False
        first_col_zero = False
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution = Solution()
    print("Original Matrix:")
    for row in matrix:
        print(row)

    solution.setZeroes(matrix)
    
    print("\nModified Matrix:")
    for row in matrix:
        print(row)
