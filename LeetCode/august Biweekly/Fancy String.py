class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        res = [s[i] for i in range(0,2)]
        for i in range(2, len(s)):
            if s[i] == s[i-2] and s[i] == s[i-1]:
                continue
            res.append(s[i])
        return ''.join(res)