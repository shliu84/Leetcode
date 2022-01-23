# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        front, behind = head, head
        
        for i in range(n):
            front = front.next
        
        if front==None:
            return head.next
        
        while front and front.next:
            front = front.next
            behind = behind.next
        
        
        behind.next = behind.next.next
            
        
        return head