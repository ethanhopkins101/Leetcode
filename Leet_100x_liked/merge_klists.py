'''
You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
 #------------------------------------------------
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[1->4->5,
  1->3->4,
  2->6]
merging them into one sorted list:
1->1->2->3->4->4->5->6
#------------------------------------------------
Example 2:
Input: lists = []
Output: []
#------------------------------------------------
Example 3:
Input: lists = [[]]
Output: []
#------------------------------------------------
#Approach:
Take the first node of each of the linked lists
and add it into a heap. When you add it to the heap
add (node.val, i) where i is the ith list
Create a dummy node head
Pop the first node from the heap and make it the
next node in the dummy-list. Remember to add the
first node from the ith linked list into the heap
since we just removed a node from this list from the heap , then repeat
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return head.next