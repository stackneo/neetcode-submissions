class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 1
        nums = set(nums)
        
        if len(nums) == 0:
            return 0
        for num in nums:
            count = 1
            if num - 1 in nums:
                continue
            else:
                while num+1 in nums:
                    count += 1
                    max_seq = max(count, max_seq)
                    num += 1
        
        return max_seq

        
        
        

        
        