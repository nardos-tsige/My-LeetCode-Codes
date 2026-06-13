# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0) # dummy node before head
        dummy.next = head
        prev, curr = dummy, head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next # skip curr
            else:
                prev = curr # move prev only if not removed
            curr = curr.next
        
        return dummy.next
