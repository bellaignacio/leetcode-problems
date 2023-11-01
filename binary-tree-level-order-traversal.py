# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        output = []

        while len(queue) > 0:
            queue_length = len(queue)
            level = []

            for i in range(queue_length):

                node = queue.popleft() # same as queue.shift() if queue is a normal array
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                output.append(level)

        return output


# from collections import deque

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         queue = deque()
#         queue.append(root)
#         output = []

#         while len(queue) > 0:
#             node = queue.popleft() # same as queue.shift() if queue is a normal array
#             if node:
#                 output.append(node.val)
#                 queue.append(node.left)
#                 queue.append(node.right)

#         return output
