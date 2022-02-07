class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if (i+1)%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even = sorted(even, reverse=True)
        odd = sorted(odd)
        numsret = []
        e,o = 0,0
        for i in range(len(nums)):
            if (i+1)%2==0:
                numsret.append(even[e])
                e+=1
            else:
                numsret.append(odd[o])
                o+=1
        return numsret