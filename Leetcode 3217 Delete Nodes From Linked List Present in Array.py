'''

Leetcode 3217 Delete Nodes From Linked List Present in Array
 
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after 
removing all nodes from the linked list that have a value that exists in nums.

 

Example 1:
        Input: nums = [1,2,3], head = [1,2,3,4,5]
        Output: [4,5]        
        Explanation: Remove the nodes with values 1, 2, and 3.

Example 2:
        Input: nums = [1], head = [1,2,1,2,1,2]
        Output: [2,2,2]
        Explanation: Remove the nodes with value 1.

Example 3:
        Input: nums = [5], head = [1,2,3,4]
        Output: [1,2,3,4]
        Explanation: No node has value 5.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Use a set for faster lookup
        num_set = set(nums)

        # Create a dummy node to build the new list
        dummy = ListNode()
        current = dummy

        # Traverse the linked list
        while head:
            # If the current node's value is in the set, skip it
            if head.val not in num_set:
                current.next = head
                current = current.next
            head = head.next

        # Terminate the new list
        current.next = None

        return dummy.next

