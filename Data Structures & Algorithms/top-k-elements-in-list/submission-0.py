class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        arr = []
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] = dictionary[num] + 1
        

        sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

        for key, val in sorted_dict:
            if k > 0:
                arr.append(key)
                k -= 1
            else:
                break
        
        return arr