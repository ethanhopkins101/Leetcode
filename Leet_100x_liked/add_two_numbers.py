'''You are given two non-empty linked lists representing two non-negative integers. The digits
 are stored in reverse order, and each of their nodes contains a single digit.
   Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''
'''
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1] '''
'''
Approach
Use Two pointers to calculate a list of output digits. Then use a for loop to "sew" the ordinary list into linked-list.
from typing import Optional
'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        increment = False
        out = ListNode()
        num_list = []
        while l1 and l2:
            num = l1.val + l2.val
            if increment:
                num += 1
            if num >= 10:
                increment = True
                num = num % 10
            else:
                increment = False
            num_list.append(num)
            l1 = l1.next
            l2 = l2.next

        while l1:
            num = l1.val
            if increment:
                num += 1
            if num >= 10:
                increment = True
                num = num % 10
            else:
                increment = False
            num_list.append(num)
            l1 = l1.next
        
        while l2:
            num = l2.val
            if increment:
                num += 1
            if num >= 10:
                increment = True
                num = num % 10
            else:
                increment = False
            num_list.append(num)
            l2 = l2.next
        if increment:
            num_list.append(1)

        head = out
        head.val = num_list[0]       
        for i in range(1, len(num_list)):
            node = ListNode()
            node.val = num_list[i]
            head.next = node
            head = head.next
        return out
            

