class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cache = {}

        for num in nums:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]

        for key, v in cache.items():
            freq[v].append(key)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                if len(res) >= k:
                    return res
                else:
                    res.append(j)

        
        return res