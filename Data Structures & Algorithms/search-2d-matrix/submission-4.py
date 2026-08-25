class Solution:
    def binarySearch(self,arr:List[int], tar :int)-> bool:
        l=0
        h=len(arr)-1
        mid = 0
        while(l<=h):
            mid = l + ((h-l)//2)
            if arr[mid] == tar:
                return True
            elif arr[mid] < tar:
                l = mid + 1
            elif arr[mid] > tar:
                h = mid - 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        h=len(matrix)-1
        mid=0
        le=len(matrix[0])-1
        print(le)
        while(l<=h):
            mid = l + ((h-l)//2)
            if (matrix[mid][0] <= target and matrix[mid][le]>=target):
                return self.binarySearch(matrix[mid],target)
            elif matrix[mid][le] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                h = mid - 1
        return False
        