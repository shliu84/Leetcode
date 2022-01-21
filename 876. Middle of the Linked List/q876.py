# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#https://www.youtube.com/watch?v=VqxB5WvQgwo
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hare, tortoise = head, head
        while (hare and hare.next):
            hare = hare.next.next
            tortoise = tortoise.next
        return tortoise
            
        
            
            
        