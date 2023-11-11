class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        results = []
        stack = [] # building solution candidate

        def _backtrack(openN, closedN):
            if openN == closedN == n:
                results.append("".join(stack)) # candidate is valid, add to results
                return

            # include open paranthesis
            if openN < n:
                stack.append("(")
                _backtrack(openN + 1, closedN)
                stack.pop() # "backtrack": undo modification, go back up one level

            # include closed paranthesis
            if closedN < openN:
                stack.append(")")
                _backtrack(openN, closedN + 1)
                stack.pop() # "backtrack": undo modification, go back up one level

        _backtrack(0, 0)
        return results
