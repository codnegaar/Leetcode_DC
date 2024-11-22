'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes 
contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
 
Example 1:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
Example 2:
        Input: l1 = [0], l2 = [0]
        Output: [0]
Example 3:
        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]
Constraints:
        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# Second solution
# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Adds two non-negative numbers represented by linked lists where each node contains a single digit.
        The digits are stored in reverse order, and each node adds up to create the final sum.

        Parameters:
        l1 (ListNode): The head of the first linked list representing a non-negative integer.
        l2 (ListNode): The head of the second linked list representing a non-negative integer.

        Returns:
        ListNode: The head of a new linked list representing the sum of the two input integers.
        """
        # Dummy node to simplify result construction.
        dummy = ListNode()
        current = dummy

        # Carry variable for managing overflow.
        carry = 0

        # Traverse through both lists until all nodes and carry are processed.
        while l1 is not None or l2 is not None or carry != 0:
            # Get current values from l1 and l2 if available.
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # Calculate the total value and update carry.
            total = val1 + val2 + carry
            carry = total // 10

            # Create the new node with the remainder value.
            current.next = ListNode(total % 10)

            # Move current pointer to the next.
            current = current.next

            # Move to the next nodes of l1 and l2 if available.
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # Return the next node of the dummy, which is the head of the resulting list.
        return dummy.next

