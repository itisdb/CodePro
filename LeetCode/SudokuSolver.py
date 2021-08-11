'''
The Simple Method that can bE used Basically this uses Hash Map techniques
'''
class Solution:
    N=9
    def isSafe(self,board,row,col,num):
        for i in range(self.N):
            if board[row][i]==num:
                return False
            if board[i][col]==num:
                return False
        startRow=row-row%3
        startCol=col-col%3
        for i in range(3):
            for j in range(3):
                if board[startRow+i][startCol+j]==num:
                    return False
        return True
    def solve(self,board,row,col):
        if row==self.N-1 and col==self.N:
            return True
        if col==self.N:
            row+=1
            col=0
        if board[row][col]!='.':
            return self.solve(board,row,col+1)
        for i in range(1,10):
            if self.isSafe(board,row,col,str(i)):
                board[row][col]=str(i)
                if self.solve(board,row,col+1):
                    return True
                board[row][col]='.'
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board,0,0)
        