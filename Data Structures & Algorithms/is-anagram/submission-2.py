class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # SOLUTION 1

        # s_dict = {}
        # t_dict = {}
        # for char in s:
        #     if char in s_dict:
        #         s_dict[char] += 1
        #     else:
        #         s_dict[char] = 1
        # for char in t:
        #     if char in t_dict:
        #         t_dict[char] += 1
        #     else:
        #         t_dict[char] = 1
        # return s_dict == t_dict

        # SOLUTION 2

        char_ideal_count = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            char_ideal_count[s[i]] = char_ideal_count.get(s[i], 0) + 1
            char_ideal_count[t[i]] = char_ideal_count.get(t[i], 0) - 1
        return all(v == 0 for v in char_ideal_count.values())
        