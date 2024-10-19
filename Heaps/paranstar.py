class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for i, c in enumerate(list(s)):
            print(stack)
            if c is '(' or c is '*':
                stack.append(c)
            elif c is ')':
                if len(stack) is 0: return False
                c2 = stack.pop()
                if c2 is '*':
                    if len(stack) and stack[-1] is ')':
                        return False
                    else:
                        stack.pop()
                elif c2 is ')': return False 
        return len(stack) is 0

print(Solution().checkValidString('(*)'))