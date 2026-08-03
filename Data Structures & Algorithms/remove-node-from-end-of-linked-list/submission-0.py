# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #create a dummy node so that we are exactly one node behing the node we want to delete
#move right by n to create a gap of n+1
#move both right and left until we reach the end 
#delete the node after left and point it to the right most node 

        dummy = ListNode(0,head)
        left,right=dummy,head

        while n>0 and right:
            right=right.next
            n-=1
        while right:
            right=right.next
            left=left.next

        left.next=left.next.next
        return dummy.next

