class Solution:
    def countArrangement(self, n: int) -> int:
        arr=[i+1 for i in range(n)]
        self.ans=0
        def DFS(arr,ind):
            if not arr:
                self.ans+=1
            for i in range(len(arr)):
                if arr[i]%ind==0 or ind%arr[i]==0:
                    DFS(arr[:i]+arr[i+1:],ind+1)
        DFS(arr,1)
        return self.ans
