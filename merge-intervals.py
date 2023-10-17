class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # need to sort intervals by each starting point
        intervals.sort()

        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start <= stack[-1][1]: # overlapping
                if start <= stack[-1][0]:
                    stack[-1][0] = start
                if end >= stack[-1][1]:
                    stack[-1][1] = end
            else: # not overlapping
                stack.append([start, end])

        return stack
