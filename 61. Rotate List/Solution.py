# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #edge cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        #find the length of the list and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        #calculate effective rotation
        k = k % length
        if k == 0:
            return head
        
        #find the node that will become the new tail
        #we need to go to position (length - k - 1) from the head
        #this node's next will become the new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        #reorganize the list
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head
