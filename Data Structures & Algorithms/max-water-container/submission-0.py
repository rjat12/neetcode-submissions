class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        max_area = 0
        while (start<end):
            area = abs(start-end) * min(heights[start],heights[end])
            #print(start,end,heights[start],heights[end],area)
            if area>max_area:
                max_area = area
            if heights[start]<=heights[end]:
                start = start + 1
            else:
                end = end - 1
        return max_area
            