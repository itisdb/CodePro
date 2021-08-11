class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == []:
            return 1
        i=1
        B=set(nums)
        while True:
            if i not in B:
                return i
            i+=1
