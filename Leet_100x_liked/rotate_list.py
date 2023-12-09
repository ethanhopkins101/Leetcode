"""
Given the head of a linked list, rotate the list to the right by k places.
#--------------------------------------
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
#--------------------------------------
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
#--------------------------------------
#Approach:
we modify the linked list in place by visiting the last node and then moving a certain number of nodes to find the new head of the linked list. The example below shows a visual of the algorithm working on the given example [1,2,3,4,5] k=2.
"""


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        # connect tail to head
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head

        # move to new head
        k = length - (k % length)
        while k > 0:
            cur = cur.next
            k -= 1

        # disconnect and return new head
        newhead = cur.next
        cur.next = None
        return newhead
