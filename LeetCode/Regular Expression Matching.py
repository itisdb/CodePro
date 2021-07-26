class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache={}
        def dp(i,j):
            if (i,j) not in cache:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i,j+2) or first_match and dp(i+1,j)
                    else:
                        ans = first_match and dp(i+1,j+1)
                cache[i,j] = ans
            return cache[i,j]
        return dp(0,0)