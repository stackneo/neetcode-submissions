import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_re = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        L = 0
        R = len(s_re)-1
        

        while L <= R:
            if s_re[L] != s_re[R]:
                return False
            L += 1
            R -= 1
        
        return True
        