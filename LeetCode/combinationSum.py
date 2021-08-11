class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if not candidates:
            return []
        candidates.sort()
        res = []
        