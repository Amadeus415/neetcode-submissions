# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #cycle linked list
        # save nodes in a set if it occurs again 
        tracker = set()
        current = head

        while current:
            
            if current in tracker:
                return True

            tracker.add(current)
            current = current.next

        return False