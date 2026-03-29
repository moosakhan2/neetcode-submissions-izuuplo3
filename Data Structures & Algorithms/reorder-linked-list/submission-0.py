# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Odd number of elements
        # 1 -> 2 -> 3 -> 4 -> 5
        # 1 -> 2 -> 3 -> 4

        # Step 1 calculate number of steps till end
        cur = head
        count = 0
        while cur.next != None:
            cur = cur.next
            count += 1
        
        cur = head
        flag = False
        while(count >= 0):
            temp = cur.next # 3
            if(flag):
                myhead.next = cur
                myhead = myhead.next
             
            else:
                flag = True
                myhead = cur 
     

        
            for i in range(count):
                cur = cur.next
           
            myhead.next = cur
            myhead = myhead.next

            cur = temp 
            count -= 2
        
        myhead.next = None

        
            


        
      

