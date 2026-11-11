class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        sort = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for key, val in count.items():
            sort[val].append(key)

        
        res = []

        for i in range(len(sort) - 1, -1, -1):
            if len(res) == k:
                return res
            
            for j in sort[i]:
                res.append(j)

        return res

