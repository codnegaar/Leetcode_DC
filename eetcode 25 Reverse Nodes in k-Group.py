
'''
Leetcode 25 Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:    
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
 

Constraints:     
     The number of nodes in the list is n.
     1 <= k <= n <= 5000
     0 <= Node.val <= 1000

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
  def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
      return None

    tail = head

    for _ in range(k):
      if not tail:  # Less than k nodes, do nothing
        return head
      tail = tail.next

    newHead = self._reverse(head, tail)
    head.next = self.reverseKGroup(tail, k)
    return newHead

  # Reverses [head, tail)
  def _reverse(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr != tail:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next

    return prev


# Second Solution
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses the nodes of a linked list in groups of size k and returns the modified list.
        
        Parameters:
        head (ListNode): The head of the linked list.
        k (int): The size of each group to be reversed.

        Returns:
        ListNode: The head of the modified linked list.
        """
        if not head:
            return None
        
        # Determine if there are at least k nodes remaining in the list.
        tail = head
        for _ in range(k):
            if not tail:
                # If there are fewer than k nodes, return the list as-is.
                return head
            tail = tail.next
        
        # Reverse the k nodes.
        new_head = self._reverse(head, tail)
        
        # Recursively call reverseKGroup for the remaining nodes.
        head.next = self.reverseKGroup(tail, k)
        
        return new_head

    def _reverse(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses the linked list from head up to (but not including) tail.

        Parameters:
        head (ListNode): The head node of the segment to be reversed.
        tail (ListNode): The node at which to stop the reversal (not inclusive).

        Returns:
        ListNode: The new head of the reversed segment.
        """
        prev = None
        current = head
        
        # Reverse the nodes until we reach the tail.
        while current != tail:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Return the new head of the reversed list (previously the tail of this segment).
        return prev


