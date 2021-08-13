class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            temp = None
            for j in range(i-1, -1, -1):
                if temp == None:
                    if nums[j] >= i - j:
                        temp = dp[j] + 1
                elif nums[j] >= i-j:
                    if temp > dp[j] + 1:
                        temp = dp[j] + 1
                        break
            if temp == None:
                dp[i] = 0
            else: dp[i] = temp
        return dp[-1]