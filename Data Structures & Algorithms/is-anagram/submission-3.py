class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

       dict_t = {}
       dict_s = {}

       if len(s) != len(t):
           return False

       for i in range(len(t)):
           if t[i] in dict_t:
               dict_t[t[i]] += 1
           else:
               dict_t[t[i]] = 1

           if s[i] in dict_s:
               dict_s[s[i]] += 1
           else:
               dict_s[s[i]] = 1
        
       return (dict_t == dict_s)