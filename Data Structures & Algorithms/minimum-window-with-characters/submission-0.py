import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        target_counts = collections.Counter(t)
        window_counts = {}

        have = 0
        need = len(target_counts)

        res = (float("inf"), 0, 0)
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the current character's frequency matches the target frequency
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # While the window is "valid" (contains all characters of t)
            while have == need:
                # Update our result if this window is smaller than the previous best
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)

                # Pop the character at 'l' to try and find a smaller window
                left_char = s[l]
                window_counts[left_char] -= 1
                
                # If removing left_char makes the window invalid
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                
                l += 1

        # Return the smallest window or an empty string if none found
        length, start, end = res
        return s[start : end + 1] if length != float("inf") else ""

            

        

