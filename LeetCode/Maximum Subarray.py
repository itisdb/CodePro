class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxm= nums[0]
        end=nums[0]
        
        for i in range(1,len(nums)):
            end=max(nums[i],end+nums[i])
            maxm=max(maxm,end)
        return maxm
        