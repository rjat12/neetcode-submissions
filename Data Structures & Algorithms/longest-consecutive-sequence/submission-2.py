class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        glb = 1
        cnt = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                cnt = cnt +1
            elif nums[i+1] - nums[i] == 0 :
                continue
            else:
                if cnt > glb:
                    glb = cnt
                    cnt = 1
                else:
                    cnt = 1
        glb = max(cnt,glb)
        return glb
        