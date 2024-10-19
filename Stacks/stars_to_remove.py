class Solution:
    def removeStars(self, s: str) -> str:
        chars = []
        for c in s:
            if c != '*': chars.append(c)
            else:
                stars_to_remove = 1
                while stars_to_remove:
                    last_char = chars.pop()
                    if last_char == '*': stars_to_remove += 1
                    stars_to_remove -= 1
        return ''.join(chars)