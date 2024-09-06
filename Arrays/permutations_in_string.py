class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        # Count characters in s1
        count_s1 = Counter(s1)

        # Initialize window in s2
        l, r = 0, 0
        count_window = Counter()

        while r < len(s2):
            # Expand window
            count_window[s2[r]] += 1
            r += 1

            # Check if window is valid
            if count_window == count_s1:
                return True

            # Shrink window if it's too large
            while r - l + 1 > len(s1):  # Window size should match s1's length
                count_window[s2[l]] -= 1
                l += 1

        return False