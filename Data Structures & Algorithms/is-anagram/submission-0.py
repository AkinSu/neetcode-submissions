class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cache_t, cache_s = {},{}
        for i in range(len(s)):
            if s[i] not in cache_s:
                cache_s[s[i]] = 0
            if t[i] not in cache_t:
                cache_t[t[i]] = 0
            
            cache_s[s[i]] += 1
            cache_t[t[i]] += 1

        return (cache_t == cache_s)
            

        