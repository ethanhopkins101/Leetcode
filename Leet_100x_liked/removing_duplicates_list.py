"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
#-----------------------------------------------
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
#-----------------------------------------------
Example 1:
Input: head = [1,1,1,2,3]
Output: [2,3]
#-----------------------------------------------
#Approach:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""


class Solution(object):
    def deleteDuplicates(self, head):
        fake = ListNode(-1)
        fake.next = head
        # We use prev (for node just before duplications begins), curr (for the last node of the duplication group)...
        curr, prev = head, fake
        while curr:
            # while we have curr.next and its value is equal to curr...
            # It means, that we have one more duplicate...
            while curr.next and curr.val == curr.next.val:
                # So move curr pointer to the right...
                curr = curr.next
            # If it happens, that prev.next equal to curr...
            # It means, that we have only 1 element in the group of duplicated elements...
            if prev.next == curr:
                # Don't need to delete it, we move both pointers to right...
                prev = prev.next
                curr = curr.next
            # Otherwise, we need to skip a group of duplicated elements...
            # set prev.next = curr.next, and curr = prev.next...
            else:
                prev.next = curr.next
                curr = prev.next
        # Return the linked list...
        return fake.next
