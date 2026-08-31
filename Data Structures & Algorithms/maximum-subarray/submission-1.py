class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        fin = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            fin = max(fin, cur)
        return fin