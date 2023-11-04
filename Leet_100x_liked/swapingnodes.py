'''
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values
in the list's nodes (i.e., only nodes themselves may be changed.)
#-------------------------------------
Example 1:
nput: head = [1,2,3,4]
Output: [2,1,4,3]
#-------------------------------------
Example 2:
Input: head = []
Output: []
#-------------------------------------
Example 3:
Input: head = [1]
Output: [1]
#-------------------------------------
#Approach:
We start by creating a dummy node to serve as the previous node for the head node.
We then iterate through the linked list, swapping pairs of nodes by updating their next pointers.
We move the previous node pointer to the first node in the pair.
The new head of the list is returned as the next node of the dummy node.
'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            first_node = head
            second_node = head.next

            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev = first_node
            head = first_node.next
        return dummy.next