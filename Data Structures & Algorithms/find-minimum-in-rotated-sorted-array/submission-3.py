class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        if nums[l] <= nums[h]:
            return nums[l]
        while(l<=h):
            mid = l+(h-l)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[h]:
                l = mid+1
            else:
                h = mid-1