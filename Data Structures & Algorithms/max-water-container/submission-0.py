class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        L = 0
        R = len(heights)-1

        while L < R:
            width = R - L
            height = min(heights[L], heights[R])
            area = height * width
            max_area = max(max_area, area)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        

        return max_area
        