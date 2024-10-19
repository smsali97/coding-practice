class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        start = 0

        curr_vowels = sum([c in vowels for c in s[:k]])
        max_vowels = curr_vowels

        for end in range(k, len(s)):
            curr_vowels += 1 if s[end] in vowels else 0
            curr_vowels += -1 if s[start] in vowels else 0
            max_vowels = max(max_vowels,curr_vowels)

            start += 1
        return max_vowels
            
