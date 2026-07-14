class Solution:

    def encode(self, strs):
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return result