class Solution:

    def find_end_digit(self,s,i):
        digits = {str(i) for i in range(10)}
        start = end = i
        while end < len(s):
            if s[end] not in digits:
                return end-1 # this is a digit
            end += 1
        return len(s) - 1

    def evaluate(self,op1,op2,operator):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        else:
            raise Exception('invalid operator')

    def calculate(self, s: str) -> int:
        operand1 = operand2 = None
        operator = None
        digits = {str(i) for i in range(10)}
        operators = {'+','-'}
        i = 0
        while i < len(s):
            c = s[i]
            print(i,c,operand1,operand2,operator)
            if c in digits:
                start_digit = i
                end_digit = self.find_end_digit(s,i)
                number = int(s[start_digit:end_digit+1])
                
                if not operator:
                    # cannot evaluate so insert it to op1
                    operand1 = number
                else:
                    if not operand1: operand1 = 0
                    operand2 = number
                    operand1 = self.evaluate(operand1,operand2,operator)
                    operator2 = operator = None # used it
                i = end_digit + 1
                continue
            if c in operators:
                operator = c
            if c == '(':
                # evaluate this first
                para_begin = i
                para_end = -1
                skip_close = 0
                for j in range(i+1,len(s)):
                    # find how many '(' are nested inside
                    if s[j] == '(': skip_close += 1
                    if s[j] == ')':
                        if skip_close: skip_close -= 1
                        else:
                            para_end = j
                            break 
                if para_end == -1: raise Exception('invalid expression ) not found ')
                sub_answer = self.calculate(s[para_begin+1:para_end])
                # insert answer at appropriate place
                if not operator:
                    # cannot evaluate so insert it to op1
                    operand1 = sub_answer
                else:
                    if not operand1: operand1 = 0
                    operand2 = sub_answer
                    operand1 = self.evaluate(operand1,operand2,operator)
                    operator2 = operator = None # used it 
                i = para_end + 1
                continue
            i += 1
        if not operand1: operand1 = 0
        return operand1 # contains final answer

