"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#----------------------------------------------
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
#----------------------------------------------
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
#----------------------------------------------
#Approach:
Check if the given list is empty, if yes, return an empty list.
Initialize an empty list named merged to store the merged intervals.
Sort the given list of intervals by the first element of each interval using the sort method and a lambda function.
Set the variable prev to the first interval of the sorted intervals list.
Iterate over the sorted intervals list, starting from the second interval.
Check if the start point of the current interval is less than or equal to the end point of the previous interval.
If yes, then update the end point of the previous interval with the maximum of the current interval's end point and the previous interval's end point.
If no, then append the previous interval to the merged list and set prev to the current interval.
After the loop, append the last interval (prev) to the merged list.
Return the merged list containing the merged intervals.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        merged = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval

        merged.append(prev)

        return merged
