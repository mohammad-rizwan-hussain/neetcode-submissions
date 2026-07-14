from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_grp = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in anagram_grp:
                anagram_grp[key].append(word)
            else:
                anagram_grp[key] = [word]
        return list(anagram_grp.values())