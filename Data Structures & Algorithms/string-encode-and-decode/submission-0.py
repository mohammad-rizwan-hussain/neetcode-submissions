class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
        result = ""
        for word in strs:
            sep = str(len(word)) + delimiter + word
            result += sep
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        num = ""
        while (i < len(s)):
            if s[i] == "#":
                shift = int(num)
                result.append("".join(s[i+1: i+shift+1]))
                num = ""
                i = i + shift + 1
            else:
                num += s[i]
                i += 1
        return result

