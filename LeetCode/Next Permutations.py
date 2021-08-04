from itertools import permutations
class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        s=int(''.join([str(x) for x in nums]))
        perm=permutations([str(x) for x in nums])
        for i in list(perm):
            if int(''.join(list(i))) > s:
                nums= list(i)
                return
        nums.reverse()

