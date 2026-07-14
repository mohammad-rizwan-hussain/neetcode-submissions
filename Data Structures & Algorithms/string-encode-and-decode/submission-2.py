class Solution:

    def encode(self, strs):
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        num = ""
        while (i < len(s)):
            if s[i] == "#":
                shift = int(num)
                result.append(s[i+1: i+shift+1])
                num = ""
                i = i + shift + 1
            else:
                num += s[i]
                i += 1
        return result
