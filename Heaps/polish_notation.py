class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric() or (token[0] == '-' and token[1:].isnumeric()):
                stack.append(int(token))
            else:
                op = token
                n1 = stack.pop()
                n2 = stack.pop() 
                if op == '+':
                    a = n1 + n2
                elif op == '-':
                    a = n2 - n1
                elif op == '*':
                    a = n1 * n2
                elif op == '/':
                    import math
                    print(n2,n1)
                    a = int(n2 / n1)
                prev = int(a)
                stack.append(prev)
        return stack[0]
