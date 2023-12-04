"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
#-------------------------------------------
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
#-------------------------------------------
Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
#-------------------------------------------
#Approach:
If it begins after our new interval ends,
Insert new interval to our output
Add all remaining intervals from the current interval to our output container.
Exit the loop by returning the currently generated output.
If it ends before our new interval begins
Add it directly to our output, as new interval does not need to be processed yet and is still yet to come somewhere in the future time intervals.
If it overlaps with our new interval
Redefine new interval
"""


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # Initialize an output container
        output = []

        # Iterate through all intervals
        for i in range(len(intervals)):
            # If the new interval ends before the current interval
            # - Append the new interval to the output
            # - Append the rest of the remaining intervals to the output
            # - Return the output
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]

            # If the new interval begins after the current interval
            # - Append the current interval to the output
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])

            # If the new interval overlaps with the current interval
            # merge intervals to create a new interval where
            # - Interval begins at the earliest of beginnings
            # - Interval ends at the latest of ends
            #
            # ! Do not add the new interval to the output just yet!
            # ! Further merging may be required
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        # Add the new interval to the output if not added already
        # ! No need for conditions as we would not reach this point otherwise
        output.append(newInterval)

        # Return the final output
        return output
