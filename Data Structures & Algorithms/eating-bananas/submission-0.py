class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        high = max(piles)
        mid=0
        while(l<=high):
            mid=l+(high-l)//2
            print(mid)
            s = 0
            for i in range(len(piles)):
                s += math.ceil(piles[i]/mid)
            if s <= h:
                high = mid - 1
            elif s > h:
                l = mid+1
                high = max(piles)
        return mid
                

        