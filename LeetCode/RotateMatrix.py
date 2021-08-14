class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix is None:
            return 
        if len(matrix)==0 or len(matrix)==1:
            return
        
        n=len(matrix)-1
        
        #matrix row flipping
        for i in range(len(matrix)//2):
            matrix[i],matrix[n]=matrix[n],matrix[i]
            n-=1
        
        #transposing the matrix
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                
        return