# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if we reach the ends of both subtrees at the same time
        if not p and not q: return True

        # if one node is null but the other is not
        elif not p or not q: return False

        # if the nodes' values do not match
        elif p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
