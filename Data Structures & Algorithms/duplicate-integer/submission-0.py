class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = 0
        for i in range(len(nums)):
            dict1[nums[i]] += 1
        for key,value in dict1.items():
            if dict1[key] > 1:
                return True
        return False