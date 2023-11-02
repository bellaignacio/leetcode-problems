# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        count = 0

        while len(queue) > 0:
            node = queue.popleft()
            if node:
                count += 1
                queue.append(node.left)
                queue.append(node.right)

        return count
