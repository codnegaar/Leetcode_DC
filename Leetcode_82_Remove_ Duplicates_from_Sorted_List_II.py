'''
Leetcode 82. Remove Duplicates from Sorted List II:

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only
distinct numbers from the original list. Return the linked list sorted as well.

solution: 
I. Keep one of the duplicates 
input: 1->2->2->3->3->4       output: 1->2->3->4

This one is pretty straight forward. We only need to check if the current node’s value is the same 
as its next node’s value. In order to do that, we keep a current node pointer. If the next node is
not None and has the same value, we skip it by changing cur.next to cur.next.next . Otherwise, we 
keep updating the cur pointer to the next node.In the end, we return head with all duplicates being skipped.

II. Keep only distinct nodes
input: 1->2->2->3->3->4       output: 1->4

Now it gets interesting. If a node’s value repeats in other nodes, we want to delete all of these nodes.
In the previous question, we only need to look at the next node. However, in this case only looking at
the next node is not enough. We have to compare with its previous value and keep a pointer at the previous
value in case if we want to delete the current node. This include the head , and that’s why we add a dummy 
node and point it to the head.

'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tempdic = {}

        temp = ListNode(0)
        temp.next = head
        
        
        while head:
            tempdic[head.val] = tempdic.get(head.val, 0) + 1            
            head = head.next
                        
        head = temp.next
        prev = temp
                
        while head:
            if tempdic[head.val] > 1:
                prev.next = head.next
            else:
                prev = head
            head = head.next
            
        return temp.next
        

