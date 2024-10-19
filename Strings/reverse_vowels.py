class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        vowels = ['a','e','i','o','u']
        lst = list(s)
        while l < r:
            if s[l].lower() not in vowels: l += 1
            elif s[r].lower() not in vowels: r -= 1
            else:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
        return ''.join(lst)