class Solution:
    def checkNextIndex(self, nums, index):
        if nums[index]==0 and index<len(nums)-1:
            return None
        if index==len(nums)-1:
            return index
        maxindex=index+1
        max=nums[index+1]
        for i in range(index+1,index+nums[index]+1):
            if i>=len(nums):
                break
            else:
                if max<nums[i]:
                    max=nums[i]
                    maxindex=i
        return maxindex    
    
    
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        index=self.checkNextIndex(nums,0)
        while index is not None:
            if nums[index]<=0:
                return False
            if index==len(nums)-1:
                return True
            index=self.checkNextIndex(nums,index)