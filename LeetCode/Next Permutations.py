class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1: return
        l, j, large, r = len(nums)-2, -1, -1, -1
        while l >= 0:
            if nums[l] < nums[l+1]:
                j, large = l+1, nums[l+1]; break
            l -= 1
        if l == -1: nums.sort(); return
        while j < len(nums):
            if nums[j] > nums[l] and nums[j] <= large:
                r, large= j, nums[j]
            j +=1
        nums[l], nums[r] = nums[r], nums[l]
        nums[l+1:] = sorted(nums[l+1:])