# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        current = head
        previous = None
        next_node = None

        while current:

            #get next node
            next_node = current.next

            #switch current pointer
            current.next = previous

            #update previous
            previous = current

            #update current
            current = next_node

            
        return previous
    
        