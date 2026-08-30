class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1 = 0
        profit = 0
        for i in range(1,len(prices)):
            start = 0
            while(start+i <= len(prices)-1):
                if prices[start]>prices[start+i]:
                    start = start + 1
                elif(prices[start+i]-prices[start]>max1):
                    max1 =  prices[start+i]-prices[start]
                    start = start + 1
                else:
                    start = start + 1
        return max1
                
                
            
            


        