class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        idx = -1
        while L <= R:
            if nums[L] == target:
                idx = L
                return idx
            elif nums[R] == target:
                idx = R
                return idx
            elif L == R:
                L += 1
                R = len(nums) - 1
            R -= 1
        

        return idx

