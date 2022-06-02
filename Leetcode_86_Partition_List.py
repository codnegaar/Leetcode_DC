'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # initiate two temporary linkedlist
        ltmp, btmp = ListNode(0), ListNode(0)
        
        # assign the values
        less, bigger, curr = ltmp, btmp, head
        while curr:
        
            # push the values in smaller values LL in comparison with x
            if curr.val < x:
                less.next = curr
                less = curr
                
            # push the values in greater values LL in comparison with x
            else:
                bigger.next = curr
                bigger = curr
                
            # move to next (iteration)
            curr = curr.next
            
        # point the last node of smaller to the head of bigger LL
        less.next, bigger.next = btmp.next, None
        return ltmp.next
        
        
