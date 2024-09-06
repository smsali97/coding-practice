class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""

        counter_t = Counter(t)
        required_chars = len(counter_t)  # Number of unique chars needed
        counter_window = Counter()  # Track chars in the current window
        formed_chars = 0  # Count of chars from t with sufficient count in window

        l, r = 0, 0
        min_window_size = float('inf')
        min_window_substr = ""

        while r < len(s):
            char_s = s[r]
            counter_window[char_s] += 1

            # If this char is needed and now has enough count, increment formed_chars
            if char_s in counter_t and counter_window[char_s] == counter_t[char_s]:
                formed_chars += 1

            # Try to shrink the window if we have all the required characters
            while l <= r and formed_chars == required_chars:
                # Update the minimum window if a smaller one is found
                if r - l + 1 < min_window_size:
                    min_window_size = r - l + 1
                    min_window_substr = s[l:r+1]

                # Shrink the window from the left
                char_l = s[l]
                counter_window[char_l] -= 1
                if char_l in counter_t and counter_window[char_l] < counter_t[char_l]:
                    formed_chars -= 1
                l += 1

            r += 1  # Expand the window to the right

        return min_window_substr if min_window_size != float('inf') else ""