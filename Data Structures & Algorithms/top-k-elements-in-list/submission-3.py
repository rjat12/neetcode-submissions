from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = Counter(nums)
        dict1r = (sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        arr=[]
        for i in range(k):
            arr.append(dict1r[i][0])
        return arr
