class Solution:

    # The code uses a sliding window approach.
    # It expands the window to the right 
    # and keeps track of the maximum count of any
    # single character within the window. 
    # If the number of characters that need replacement exceeds k,
    # the window is shrunk from the left until the condition is satisfied. 
    # The maximum window size encountered during this process is the answer.

    def characterReplacement(self, s: str, k: int) -> int:
        # ABAB, k = 2

        # AB
        # AA (1) or BB (1)
        # next character is  A
        # AAA
        # AAAA (0)
        from collections import defaultdict
        l, r = 0,0
        counts = defaultdict(int)
        max_window = 0 # global max window
        max_count = 0  # Track the maximum count of any single character in the window
        while r < len(s):
            counts[s[r]] += 1

            max_count = max(max_count, counts[s[r]])  # Update max_count
            
            
            while (r-l+1) - max_count > k:
                counts[s[l]] -= 1
                l += 1
            
            max_window = max(max_window,r-l+1)

            r += 1
        return max_window