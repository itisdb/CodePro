class Solution:
    def dfs(self,dp, boxes, left, right, length):
        if left>right:
            return 0

        elif left==right:
            return (length+1)*(length+1)

        elif dp[left][right][length]!=0:
            return dp[left][right][length]
        
        else:
            m=self.dfs(dp,boxes,left+1,right, 0)+(length+1)*(length+1)

            for i in range(left+1,right+1):
                if boxes[left]==boxes[i]:
                    m=max(m, self.dfs(dp,boxes, left+1,i-1,0)+self.dfs(dp,boxes,i,right,length+1))

            dp[left][right][length]=m            
            return m


    def removeBoxes(self, boxes: List[int]) -> int:
        if boxes is None:
            return 0
        if len(boxes)==1:
            return 1
        '''
        do not touch a group at all or delete it entirely in whatever
        order that makes more sense. 
        '''
        dp=[[[0 for _ in range(len(boxes))]for __ in range(len(boxes))]for ___ in range(len(boxes))]

        return self.dfs(dp,boxes,0,len(boxes)-1,0)

