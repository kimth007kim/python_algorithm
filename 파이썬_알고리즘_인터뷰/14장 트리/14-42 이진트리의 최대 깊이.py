# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        q = deque()
        q.append([root, 1])

        while q:
            now, cnt = q.popleft()
            result = max(result, cnt)
            if now.left != None:
                q.append([now.left, cnt + 1])
            if now.right != None:
                q.append([now.right, cnt + 1])
        return result