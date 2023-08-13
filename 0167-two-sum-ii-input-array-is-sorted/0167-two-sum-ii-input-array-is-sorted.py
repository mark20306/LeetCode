class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            res = target - numbers[i]
            if res in hashmap:
                return [hashmap[res]+1 , i+1]
            hashmap[numbers[i]] = i 
        return [0,0]        