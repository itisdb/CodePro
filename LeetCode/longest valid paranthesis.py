class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                dp[i] = 0
            elif s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
        return max(dp)