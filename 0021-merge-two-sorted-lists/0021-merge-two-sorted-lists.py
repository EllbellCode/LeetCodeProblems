# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = ListNode()
        tail = merged

        #While there are elements still in both lists
        while list1 and list2:
            if list1.val < list2.val:
                #Set the tail to the reference of list 1
                tail.next = list1
                #Move list 1 to the next value
                list1 = list1.next
            else:
                #same as above but for list2
                tail.next = list2
                list2 = list2.next
            
            #Move the tail to the last element 
            #which will be the reference to the last list it added
            tail = tail.next

        #After one list has run out of elements
        #Add the remainder of the other list
        tail.next = list1 if list1 else list2

        #merged.next will contain the merged list
        return merged.next



        