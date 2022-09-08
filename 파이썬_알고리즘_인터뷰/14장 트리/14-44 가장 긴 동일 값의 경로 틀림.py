# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = 1

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):

            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.right:
                print(node.val, node.left.val, node.right.val)
            elif node.left and not node.right.val:
                print(node.val, node.left.val, None)
            elif not node.left and node.right:
                print(node.val, None, node.right.val)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result
