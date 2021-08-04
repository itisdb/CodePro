class Solution:
			def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
				if not root:
					return []
				return self.dfsTargetSum(root,targetSum,[],[])
			def dfsTargetSum(self,root,s,ans,path):
				if not root:
					return None
				if not root.left and not root.right and root.val==s:
					path.append(ans+[root.val])
				self.dfsTargetSum(root.left,s-root.val,ans+[root.val],path)
				self.dfsTargetSum(root.right,s-root.val,ans+[root.val],path)
				return path