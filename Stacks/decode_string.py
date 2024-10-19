class Solution:
    def decodeString(self, s: str) -> str:
        """
        3[a]2[bc]
        3 times x [ ...] 2 x [ ...]
        
        find first square bracket, call it index i
        everything left of i is the number
        and then until you encounter a closing repeat it that

            issue: what if inside nested opening
            open a new call stack whenever you encounter an opening brace
        """
        stack = []
        digits = { str(i) for i in range(0,10) }
        i, n = 0, len(s) 
        while i < n:
            char = s[i]
            if char in digits:
                number = ''
                while char in digits:
                   number += char
                   i += 1
                   char = s[i]
                number = int(number)
                stack.append(number)
                continue
            elif char != ']':
                stack.append(char)
            else:
                opening_found = False
                output_str = ''
                while not opening_found:
                    char = stack.pop()
                    opening_found = '[' == char
                    if not opening_found: output_str = char + output_str
                stack.append(output_str * stack.pop()) # str * number
            i += 1
        return ''.join(stack)



            