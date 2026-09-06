class Solution:
    def sortArray(self,arr):
        arr = sorted(arr,reverse=True)
        return arr
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        arr = self.sortArray(stones)
        while(len(arr)>1):
            arr = sorted(arr,reverse=True)
            print(arr)
            if arr[0] == arr[1]:
                arr.pop(0)
                arr.pop(0)
            elif arr[0] > arr[1]:
                p = arr[0]
                arr.pop(0)
                arr[0] = p - arr[0]
            elif arr[1] > arr[0]:
                p = arr[1]
                arr.pop(1)
                arr[0] = p - arr[0]
        if arr:
            return arr[0]
        else:
            return 0        