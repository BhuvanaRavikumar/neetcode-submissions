# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #need to split the linked list into 2 and find the middle 
        #lets use slow and fast pointers for this 
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #get the middle and reverse the second half
        second=slow.next
        prev=slow.next=None

        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp

        #merge the two linked lists by taking one from the beginning and one from the end 

        first,second=head,prev
        while second:
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first,second=temp1,temp2

        