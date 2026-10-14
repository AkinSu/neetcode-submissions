class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0 , -1):
            for j in freq[i]:
                if len(res) < k:
                    res.append(j)
                else:
                    return res
            
        return res
            
        