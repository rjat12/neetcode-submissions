class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        print(nums)
        if not nums or len(nums) < 3 :
            return ans
        for i in range(0,len(nums)-2):
            left = i+1
            right = len(nums)-1
            target = nums[i]
            while (left < right):
                if nums[left]+nums[right]+target == 0:
                    if [target,nums[left],nums[right]] not in ans:
                        ans.append([target,nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif (nums[left]+nums[right]<(-1*target)):
                    left += 1
                elif (nums[left]+nums[right]>(-1 * target)):
                    right -= 1
        return ans