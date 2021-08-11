class Solution:
    def dfs(self, nums, target, path, res):
        if target < 0:
            return
        if target == 0:
            if path not in res:
                res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:], target - nums[i], path + [nums[i]], res)
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], res)
        return res