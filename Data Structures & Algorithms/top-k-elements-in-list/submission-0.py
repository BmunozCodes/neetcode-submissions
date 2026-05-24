from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_pairs = sorted(count.items(), key = lambda x: x[1], reverse = True)
        return [pair[0] for pair in sorted_pairs[:k]]

        