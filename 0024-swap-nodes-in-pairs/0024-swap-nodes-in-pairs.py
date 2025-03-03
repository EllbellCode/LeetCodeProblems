# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        dummy.next = head
        tail = dummy

        while head and head.next:

            # select the next two nodes
            odd = head
            even = head.next

            #Put the second node first
            tail.next = even
            #Have first node point to where the second node points
            odd.next = even.next
            #Have second node point to where first node points
            even.next = odd

            # Move pointers forward
            
            #Set tail to odd as the next pair is after odd
            tail = odd
            #next unswapped node in the list
            head = odd.next

        return dummy.next





            
        
        