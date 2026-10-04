class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        cache = {}

        for s in strs:
            ss = "".join(sorted(s))
            if ss not in cache:
                cache[ss] = []
            
            cache[ss].append(s)

        return cache.values()