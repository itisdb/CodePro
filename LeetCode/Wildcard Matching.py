class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p==s: 
            return True
        if len(p)==0:
            return False
        if p=='*':
            return True
        if s=='':
            return False
        dp=[[False for i in range(len(s))] for j in range(len(p))]
        for i in range(0,len(p)+1,-1):
            for j in range(0,len(s)+1,-1):
                if j==len(s) and i==len(p):
                    dp[i][j]=True
                elif i==len(p):
                    dp[i][j]=False
                elif j==len(s):
                    if p[i]=='*':
                        dp[i][j]=dp[i+1][j]
                    else:
                        dp[i][j]=False
                else:
                    if p[i]=='*':
                        dp[i][j]=dp[i+1][j] or dp[i][j+1]
                    elif p[i]=='?' or p[i]==s[j]:
                        dp[i][j]=dp[i+1][j+1]
                    else:
                        dp[i][j]=False
        return dp[0][0]             
                