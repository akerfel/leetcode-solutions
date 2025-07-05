# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]

    # returns [isBalanced, height]
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return [True, 0]

        leftBalanced, leftHeight = self.dfs(root.left)
        rightBalanced, rightHeight = self.dfs(root.right)
        isBalanced = leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1

        height = 1 + max(leftHeight, rightHeight)
        return [isBalanced, height]
