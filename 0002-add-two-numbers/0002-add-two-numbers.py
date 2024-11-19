# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#self is just the example name of the linked list to show how you use the val and next commands
# val is the initialised value of the current node
# next is the next node in the linked list
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        dummy = ListNode(0)  # Placeholder for the result linked list
        current = dummy
        carry = 0 # initialise carry value

        while l1 or l2 or carry:
            
            # Extract values from nodes, or use 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute the sum and carry
            total = val1 + val2 + carry
            carry = total // 10 #Carry is 1 or 0, 1 when the sum of the single digits leads to a double digit output
            current.next = ListNode(total % 10)

            # Move to the next nodes
            current = current.next
            if l1: #If there is another value in the linked list it moves on
                l1 = l1.next
            if l2: #If there is another value in the linked list it moves on
                l2 = l2.next

        return dummy.next  # Skip the dummy node


        