class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        cache = {}
        for i in range(len(nums)):
            if nums[i] in cache:
                return True
            else:
                cache[nums[i]] = 0
        
        return False
         