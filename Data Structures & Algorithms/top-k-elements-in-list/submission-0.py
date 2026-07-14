from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list_freq = Counter(nums)
        sorted_freq_list = sorted(list_freq.items(), key=lambda item:item[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_freq_list[i][0])
        return result