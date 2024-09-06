class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABAB, k = 2

        # AB
        # AA (1) or BB (1)
        # next character is  A
        # AAA
        # AAAA (0)
        from collections import defaultdict
        l, r, max_window = 0,0,0
        counts = defaultdict(int)
        # letters = [chr(ord('A')+i) for i in range(26)]
        max_window = 0
        def get_most_freq():
            k_max, v_max = max(counts.items(),key=lambda x: x[1])
            return (k_max, v_max)
        
        max_count = 0  # Track the maximum count of any single character in the window
        while r < len(s):
            counts[s[r]] += 1

            max_count = max(max_count, counts[s[r]])  # Update max_count
            
            
            # while (r-l+1) - get_most_freq()[1] > k:
            while (r-l+1) - max_count > k:
                counts[s[l]] -= 1
                l += 1
            
            max_window = max(max_window,r-l+1)

            r += 1
        return max_window