from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_freq_list = sorted(Counter(nums).items(), key=lambda item:item[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_freq_list[i][0])
        return result