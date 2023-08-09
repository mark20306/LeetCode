class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = []
        n = Counter(nums)
        nlist = n.most_common(k)
        
        hashmap = [num for num,_ in nlist]
        return hashmap    
             