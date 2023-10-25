# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        def _helper(head, prev):
            if head is None:
                return prev
            next = head.next
            head.next = prev
            return _helper(next, head)

        return _helper(head, prev)

# head = (1)
# prev = None
# --> _helper((1), None)
#     next = (2)
#     (1) --> (None)
#     --> _helper((2), (1))
#         next = (3)
#         (2) --> (1)
#         --> _helper((3), (2))
#             next = (4)
#             (3) --> (2)
#             --> _helper((4), (3))
#                 next = (5)
#                 (4) --> (3)
#                 --> _helper((5), (4))
#                     next = None
#                     (5) --> (4)
#                     --> _helper((None), (5))
#                         return (5) # head of reversed linked list
