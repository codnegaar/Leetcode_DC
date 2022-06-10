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
                heapq.heappush(h, (lst.val, cnt, lst))
                cnt += 1
        while(len(h)):
            smallestPnt = heapq.heappop(h)[2]
            p.next = smallestPnt
            p = p.next
            if smallestPnt.next:
                heapq.heappush(h, (smallestPnt.next.val, cnt, smallestPnt.next))
                cnt += 1
        return ret.next
