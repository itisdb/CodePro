class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N==1: return [1]
        
        l=self.beautifulArray(N//2)
        r=self.beautifulArray(N-N//2)
        return [i*2 for i in l]+[i*2-1 for i in r]
        
 