"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
#----------------------------------------------------
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
#----------------------------------------------------
Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
#----------------------------------------------------
#Approach:
Initialize two new linked lists, less and greater, to hold nodes with values less than x and greater than or equal to x, respectively.
Traverse the original linked list, head, and for each node:
If the node's value is less than x, append it to the less list.
If the node's value is greater than or equal to x, append it to the greater list.
After traversing the original list, attach the greater list to the end of the less list.
Set the last node of the greater list's next pointer to nullptr to terminate the list.
Return the less list's head as the result.
"""


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        current = head  # Pointer to traverse the original list

        less_dummy = ListNode(0)  # Dummy node for nodes < x
        less_tail = less_dummy  # Tail pointer for less list

        greater_dummy = ListNode(0)  # Dummy node for nodes >= x
        greater_tail = greater_dummy  # Tail pointer for greater list

        # Traverse the original list
        while current:
            if current.val < x:
                # Append current node to the less list
                less_tail.next = ListNode(current.val)
                less_tail = less_tail.next  # Move the tail pointer
            else:
                # Append current node to the greater list
                greater_tail.next = ListNode(current.val)
                greater_tail = greater_tail.next  # Move the tail pointer
            current = current.next  # Move to the next node

        # Attach the greater list to the end of the less list
        less_tail.next = greater_dummy.next

        # Return the modified list starting from the first node after the less dummy node
        return less_dummy.next
