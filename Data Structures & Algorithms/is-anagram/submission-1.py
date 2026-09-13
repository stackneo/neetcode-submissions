class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        t_dict = {}

        for text in s:
            if text not in s_dict:
                s_dict[text] = 1
            else:
                s_dict[text] = s_dict[text] + 1
        

        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] = t_dict[char] + 1
        

        return s_dict == t_dict
        