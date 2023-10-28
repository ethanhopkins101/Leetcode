'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
#------------------------------------------
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
#------------------------------------------
Example 2:
Input: head = [1], n = 1
Output: []
#------------------------------------------
Example 3:
Input: head = [1,2], n = 1
Output: [1]
# Approach:
Count the total number of nodes in the linked list by traversing it with a curr pointer.
Calculate the position to move from the front to reach the node n positions from the end.
Reset the count and curr to traverse the list again.
If the node to be removed is the first node, return head.next.
Traverse the list while keeping track of the count.
When the count matches the calculated position before the node to be removed, update the connection to skip the node.
Exit the loop after performing the removal.
Return the updated head.
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        check = count - n - 1
        count = 0
        curr = head

        # Removing the first node
        if check == -1:  
            return head.next

        while curr:
            if count == check:
                curr.next = curr.next.next
                # As the removal is done, Exit the loop
                break  
            curr = curr.next
            count += 1

        return head