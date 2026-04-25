# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return []
        
        length = 1
        
        src = head.next # 2
    
        while src != None:
            length+=1 # Length = 4
            src = src.next # 4
        
        length -= n

        if length == 0:
            head = head.next
            return head
        
        prev_ = head
        next_ = head.next

        for i in range(length-1): # 2
            prev_ = next_
            next_ = next_.next
        
        prev_.next = next_.next

        return head
           





        