class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        table=[[0 for j in range(n)] for i in range(n)]
        max_len=1
        max_str=""
        i=0
        while i<n-1:
            if s[i]==s[i+1]:
                table[i][i+1]=True
                max_len=2
                max_str=s[i:i+2]
            i+=1
        k=3
        while k<n:
            i=0
            while i<n-k+1:
                j=i+k-1
                if s[i]==s[j] and table[i+1][j-1]:
                    table[i][j]=True
                    if k>max_len:
                        max_len=k
                        max_str=s[i:j+1]
                i+=1
            k+=1
        return max_str
