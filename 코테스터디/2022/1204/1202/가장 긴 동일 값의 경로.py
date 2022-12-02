# https://leetcode.com/problems/longest-univalue-path/
class Solution:
    result = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            l, r, now = None, None, None
            if node.left:
                l = node.left.val

            if node.right:
                r = node.right.val
            if node:
                now = node.val

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            print(now, l, r, "    ", left, right)
            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
