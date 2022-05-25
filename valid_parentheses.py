# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

 


class Solution:
    def isValid(self, s: str) -> bool:
        vals = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in vals.values():
                stack.append(c)
            else:
                expected_bracket = stack.pop() if len(stack) >= 1 else None
                if expected_bracket is None or c not in vals: return False
                received_bracket = vals[c]
                if expected_bracket != received_bracket: return False
        return len(stack) == 0

        