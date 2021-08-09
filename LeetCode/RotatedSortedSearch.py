class Solution:
    def findPivot(self, nums):
        
        lo, hi = 0, len(nums)-1
        
        while(lo < hi):
            mid = lo + ((hi-lo)//2)
            if mid > 0 and nums[mid-1] > nums[mid]:
                return mid
            
            if nums[0] > nums[mid]:
                hi = mid-1
                
            else:
                lo = mid+1
                
        return lo
    def findIndex(self, nums, start, end, target):
        
        lo, hi = start, end
        while(lo <= hi):
            mid = lo + ((hi-lo)//2)
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
                
        return -1
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pi = self.findPivot(nums)
        if nums[pi] == target:
            return pi
        
        loc1 = self.findIndex(nums, 0, pi-1, target)
        if loc1!=-1:
            return loc1
        loc2 = self.findIndex(nums, pi+1, len(nums)-1, target)
        return loc2