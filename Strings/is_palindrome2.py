class Solution:
    def isPalindrome(self, s: str) -> bool:
         # race a c car
         # l          r

        if len(s) <= 1:
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if not s[l].lower() == s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True