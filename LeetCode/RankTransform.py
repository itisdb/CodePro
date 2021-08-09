class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        n = len(matrix)
        m = len(matrix[0])
        rank = [0] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    rank[j] += 1
        for i in range(m):
            if rank[i] == n:
                for j in range(n):
                    matrix[j][i] = 1
            else:
                for j in range(n):
                    matrix[j][i] = 0
        return matrix
