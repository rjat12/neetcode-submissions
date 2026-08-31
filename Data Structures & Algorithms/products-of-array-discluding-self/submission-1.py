import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = math.prod(nums)
        arr = []
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] != 0:
                    arr.append(0)
                else:
                    nums[i] = 1
                    pr1 = math.prod(nums)
                    nums[i] = 0
                    arr.append(pr1)
        else:
            for i in nums:
                arr.append(int(pr/i))
        return arr