class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c={}
        r={}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    if i in r:
                        r[i]+=1
                    else:
                        r[i]=1
                    if j in c:
                        c[j]+=1
                    else:
                        c[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in r or j in c:
                    matrix[i][j]=0
        return matrix