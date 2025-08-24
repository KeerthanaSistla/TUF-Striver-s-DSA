from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result

        first_row = [1]
        result.append(first_row)

        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            result.append(current_row)

        return result

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    numRows1 = 5
    print(f"Input: numRows = {numRows1}")
    output1 = solution.generate(numRows1)
    print(f"Output: {output1}\n")
    
    # Example 2
    numRows2 = 1
    print(f"Input: numRows = {numRows2}")
    output2 = solution.generate(numRows2)
    print(f"Output: {output2}")
