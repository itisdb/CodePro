class Solution:
    def minCut(self, a: str) -> int:
        dp = [0 for i in range(len(a))]
        palindrome = [[False for i in range(len(a))] for j in range(len(a))]
        for i in range(len(a)):
            minCut = i;
            for j in range(i + 1):
                if (a[i] == a[j] and (i - j < 2 or palindrome[j + 1][i - 1])):      
                    palindrome[j][i] = True;
                    minCut = min(minCut,0 if  j == 0 else (dp[j - 1] + 1));
            dp[i] = minCut;  
        return dp[len(a) - 1];
