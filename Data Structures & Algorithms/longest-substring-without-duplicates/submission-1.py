class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        window_state = set()
        max_substring = 0

        for R in range(len(s)):
            char = s[R]
            while char in window_state:
                window_state.remove(s[L])
                L += 1
            
            window_state.add(char)
            max_substring = max(max_substring, R - L + 1)
        
        return max_substring

            
