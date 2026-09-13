class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            calc = numbers[L] + numbers[R]
            if calc == target:
                return [L+1,R+1]
            elif calc > target:
                R -= 1
            elif calc < target:
                L += 1
        