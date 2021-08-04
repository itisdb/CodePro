# Definition for a binary tree node.
from importlib.resources import path


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def dfsTargetSumPath(self, root, target, path, res):
        if root is None:
            return []
        path.append(root.val)
        sum(path)
        if root.left is None and root.right is None and sum(path) == target:
            res.append(path.copy())
        if root.left is None and root.right is not None:
            root=self.dfsTargetSumPath(root.right, target, path, res)
        if root.left is not None and root.right is None:
            root=self.dfsTargetSumPath(root.left, target, path, res)
        path.pop()
        return res
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        res = []
        path=[]
        res=self.dfsTargetSumPath(root, targetSum, path, res)
        return res

