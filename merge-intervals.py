class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # need to sort intervals by each starting point
        intervals.sort()

        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start <= stack[-1][1]: # overlapping
                if start < stack[-1][0]:
                    stack[-1][0] = start
                if end > stack[-1][1]:
                    stack[-1][1] = end
            else: # not overlapping
                stack.append([start, end])

        return stack


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()

#         stack = [intervals[0]]

#         for i in range(1, len(intervals)):
#             curr_int = {
#                 'start': intervals[i][0],
#                 'end': intervals[i][1]
#             }
#             last_int = {
#                 'start': stack[-1][0],
#                 'end': stack[-1][1]
#             }

#             if curr_int['start'] <= last_int['end'] and curr_int['end'] > last_int['end']:
#                 stack[-1][1] = curr_int['end']
#             elif curr_int['start'] > last_int['end']:
#                 stack.append(intervals[i])

#         return stack
