class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return ['']
        if n==1:
            return ["()"]
        res=[]
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    res.append('({}){}'.format(left,right))
        return res