class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        i = len(S) - 1
        j = len(T) - 1
        
        skip_s = 0
        skip_t = 0
        
        while i >= 0 or j >= 0:
            if i >= 0 and S[i] == '#':
                skip_s += 1
                i -= 1  
            elif j >= 0 and T[j] == '#':
                skip_t += 1
                j -= 1
            elif skip_s > 0 or skip_t > 0:
                if skip_s > 0:
                    i -= 1
                    skip_s -= 1
                if skip_t > 0:
                    j -= 1
                    skip_t -= 1
            else:
                if S[i] == T[j]:
                    i -= 1
                    j -= 1
                else: return False
        return True
        