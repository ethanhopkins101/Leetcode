"""
Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end,
should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
#-----------------------------------------
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
#-----------------------------------------
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
#-----------------------------------------
#Approach:
Create two pointers l and r to locate the range to be reversed.
Use jump to keep track of the position where two k-group linked list should be connected.
While r is not None and count < k, move r to the end of the k-group linked list.
If count == k, reverse the k-group linked list and connect to the previous one using jump.
If count != k, return the dummy.next, which is the head of the modified linked list.
"""


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next
