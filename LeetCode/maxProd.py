# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
      tsum=0 #the total sum of the entire tree
      maxprod=0 # the maximum product that is available for the tree 

      def dfs(root): #function for finding the total sum of the root using DFS
        if root == None: 
          return
        dfs(root.left)
        dfs(root.right)
        self.tsum+=root.val

      def calculateSubTreeSum(root): # funstion for finding the subTree sum using DFS
        if root == None:
          return 0
        l=calculateSubTreeSum(root.left)
        r=calculateSubTreeSum(root.right)
        subTreeSum=l+r+root.val
        self.maxprod=max(self.maxprod, (subTreeSum)*(self.tsum-subTreeSum))
        return subTreeSum

      dfs(root) #finding the total sum
      calculateSubTreeSum(root) #finding the subtree sum
      return int(maxprod % int(pow(10,9)+7))  #returning the value