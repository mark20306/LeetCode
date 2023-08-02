class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        '''print(sorted(count.values()))
        print(set(count.values()))'''
        if len(sorted(count.values())) == len(set(count.values())):
            return True
