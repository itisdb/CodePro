class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flip0 = flip1 = 0
        for c in s:
            flip0+=int(c=='1')
            flip1=min(flip0,flip1+int(c=='0'))
        return flip1

