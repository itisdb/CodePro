# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count=0

    def dfs(self, root, maxVal):

        #checking for the last node
        if root is None:
            return
        
        if maxVal <= root.val:
            self.count+=1

        maxVal=max(root.val,maxVal)

        self.dfs(root.left,maxVal)
        self.dfs(root.right,maxVal)
        

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root,float('-inf'))

        return self.count