class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        tsum=0

        def sumMat(matrix):
            s=0
            for i in matrix:
                s+=sum(i)
            return s
        
        def returnMax(matrix):
            val=matrix
            for i in range(len(val)-1):
                for j in range(len(val)-1):
                    