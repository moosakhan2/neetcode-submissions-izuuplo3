# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        if head == None:
            return False
        
        dummy = head
        while(dummy != None):
            visited.add(dummy)
            dummy = dummy.next
            if dummy in visited:
                return True
        
        return False
        