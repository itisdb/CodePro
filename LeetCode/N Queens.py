class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = set()
        diagonal1 = set()# 45 degrees, row - column = const
        diagonal2 = set()# the other one, row + column = const
        def backtrack(row):
            if row == n:
                return 1
            else:
                total = 0
                for col in range(n):
                    if col in columns or row - col in diagonal1 or row + col in diagonal2:
                        continue
                    columns.add(col)
                    diagonal1.add(row - col)
                    diagonal2.add(row + col)
                    total += backtrack(row+1)
                    columns.remove(col)
                    diagonal1.remove(row - col)
                    diagonal2.remove(row + col)
                return total
        return backtrack(0)