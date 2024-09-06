from collections import Counter
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        def is_repeating(s):
            c = Counter(s)
            for k, v in c.items():
                if v > 1:
                    return True
            return False
        
        left_ptr = 0
        right_ptr = 0
        max_len = 0
        # doesnt reach the end
        while right_ptr < len(s):
            # increment right pointer
            right_ptr += 1
            # get substring
            sub_str = s[left_ptr:right_ptr]
            print(sub_str)
            repeating = is_repeating(sub_str)
            if not repeating:
                max_len = max(max_len,len(sub_str))
            else:
                left_ptr += 1
        return max_len
    