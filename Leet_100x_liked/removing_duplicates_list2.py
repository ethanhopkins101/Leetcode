"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
#--------------------------------------------------
Example 1:
Input: head = [1,1,2]
Output: [1,2]
#--------------------------------------------------
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
#--------------------------------------------------
#Approach:
Handling Edge Cases: First, I checked if the list is empty because an empty list, by default, has no duplicates.
Traversal with Duplicate Removal: Starting from the head, I iterated through the list. For each node, I looked ahead to find the next distinct value (skipping over any duplicates). This was akin to hopping over redundant elements to find the next unique item in a sorted collection.
Relinking Nodes: After identifying the next distinct node, I linked the current node directly to it, effectively removing the duplicates in-between. This step is crucial as it maintains the integrity of the list while discarding duplicates.
Proceeding to Next Node: I then moved to the next distinct node and repeated the process until the end of the list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list is empty, simply return the head
        if not head:
            return head

        current = head

        while current and current.next:
            # Find the next distinct element by skipping duplicates
            next_distinct = current.next

            while next_distinct and current.val == next_distinct.val:
                next_distinct = next_distinct.next

            # Link the current node to the next distinct node
            current.next = next_distinct

            # Move to the next node in the list
            current = next_distinct

        return head
