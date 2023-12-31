'''
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''
'''
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
------------------------------------------
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
#Approach
'''
sorting a tuple of two lists by length,
 not sorting each list. It just assigns the shorter list to a and the longer to b. In the second case,
   I'm just sorting a list of up to four values.
'''
class Solution:
   def findMedianSortedArrays(self, nums1, nums2):
    a, b = sorted((nums1, nums2), key=len)
    m, n = len(a), len(b)
    after = (m + n - 1) // 2
    i = bisect_left(range(m), True, key=lambda i: after-i-1 < 0 or a[i] >= b[after-i-1])
    nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
    return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0