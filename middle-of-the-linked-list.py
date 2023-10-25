# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        node = head

        while node.next:
            node = node.next
            length += 1

        mid = (length // 2) + 1

        i = 1
        result = head

        while i < mid:
            result = result.next
            i += 1

        return result
