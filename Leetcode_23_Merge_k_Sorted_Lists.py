'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:    Input: lists = [[1,4,5],[1,3,4],[2,6]]   ->  Output: [1,1,2,3,4,4,5,6]

Explanation: The linked-lists are:
[ 1->4->5,  1->3->4,  2->6 ], merging them into one sorted list: 1->1->2->3->4->4->5->6

'''

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret = ListNode()
        p = ret
        h = []
        cnt = 0
        for lst in lists:
            if lst:
                
               #  heapq.heappush(heap, item): Push the value item onto the heap, maintaining the heap invariant.
                heapq.heappush(h, (lst.val, cnt, lst))
                cnt += 1
        while(len(h)):
            
            # Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. 
            # To access the smallest item without popping it, use heap[0].
            
            smallestPnt = heapq.heappop(h)[2]
            p.next = smallestPnt
            p = p.next
            if smallestPnt.next:
                heapq.heappush(h, (smallestPnt.next.val, cnt, smallestPnt.next))
                cnt += 1
        return ret.next
