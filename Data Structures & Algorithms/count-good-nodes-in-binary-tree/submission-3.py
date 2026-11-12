# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def goodNodes(self, root: TreeNode) -> int:
    msf = float('-inf')
    self.total = 0
    

    def dfs(root, msf):
      if not root:
        return 0
      if root.val>=msf:
        msf = root.val
        self.total+=1
      dfs(root.left, msf)
      dfs(root.right, msf)

    dfs(root, msf)

    return self.total


            