from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        x = set()
        y = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    x.add(i)
                    y.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in x or j in y:
                    matrix[i][j] = 0

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
