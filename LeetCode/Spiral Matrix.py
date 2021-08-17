class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row_up = 0
        row_down = len(matrix) - 1
        col_left = 0
        col_right = len(matrix[0]) - 1
        total = len(matrix) * len(matrix[0])
        while True:
            for i in range(col_left, col_right + 1):
                ans.append(matrix[row_up][i])
            
            for i in range(row_up + 1, row_down):
                ans.append(matrix[i][col_right])
            
            if len(ans) < total:
                for i in range(col_right, col_left - 1, -1):
                    ans.append(matrix[row_down][i])
            
            if len(ans) < total:
                for i in range(row_down - 1, row_up, -1):
                    ans.append(matrix[i][col_left])
            
            if row_up < row_down:
                row_up += 1
                row_down -= 1
            
            if col_left < col_right:
                col_left += 1
                col_right -= 1
                
            if len(ans) == total:
                return ans