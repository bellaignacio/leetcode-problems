class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: # immediately invalid - can't have matching parentheses if length is odd
            return False

        stack = []

        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for p in s:
            if p not in close_to_open: # then p is an open parentheses
                stack.append(p)
            elif not stack or stack[-1] != close_to_open[p]: # if stack has no open parentheses or the most recent one is not p's match
                return False
            else: # then p has a match, clear both
                stack.pop()

        return len(stack) == 0 # no leftover open parentheses


# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False

#         # elif s[0] in (')', '}', ']'):
#         #     return False

#         else:
#             open = []

#             for p in s:
#                 if p in ('(', '{', '['):
#                     open.append(p)
#                 elif p == ')' and len(open) > 0 and open[-1] == '(':
#                     open.pop()
#                 elif p == '}' and len(open) > 0 and open[-1] == '{':
#                     open.pop()
#                 elif p == ']' and len(open) > 0 and open[-1] == '[':
#                     open.pop()
#                 else:
#                     return False

#             return len(open) == 0
