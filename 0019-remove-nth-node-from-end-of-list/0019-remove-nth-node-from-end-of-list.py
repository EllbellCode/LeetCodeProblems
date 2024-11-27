# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):

        # Create a dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
    
        # Advance the first pointer to the n+1th node in dummy
        #ie if head = [1,2,3,4,5] and n=2 then we end on node 3 
        for _ in range(n + 1):
            first = first.next
    
        # Move both pointers until the first reaches the end
        # Since there are n+1 nodes between the first and second pointer
        #Then when the first pointer reches the end, the second pointer will be on the n+1th node from the end of the list
        while first is not None:
            first = first.next
            second = second.next
    
        #Here, we can change the n+1th node from the end of the list
        #to point to the n-1th node from the end of the lost
        #so that it skips the nth node from the end
        second.next = second.next.next
    
        # Return the modified list
        return dummy.next
        