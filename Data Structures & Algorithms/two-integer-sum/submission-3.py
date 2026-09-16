class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = 0
        R = len(nums) - 1

        while L <= R:
            add = nums[L] + nums[R]

            if add == target and L != R:
                return [L,R]

            elif L == R:
                L += 1
                R = len(nums) - 1
            else:
                R -= 1
        