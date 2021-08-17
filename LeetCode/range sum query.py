class NumArray:
    res=[]

    def __init__(self, nums: List[int]):
        self.sums = [0] + list(itertools.accumulate(nums))


    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)