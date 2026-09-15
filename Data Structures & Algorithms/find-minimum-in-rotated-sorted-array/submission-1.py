class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        track = float('inf')

        if len(nums) == 1:
            return nums[0]
        while L < R:
            M = L + (R - L) // 2
            track = min(track, nums[L], nums[M], nums[R])

            L += 1
            R -= 1
        
        return track



        