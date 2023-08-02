class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        key1 = sorted(count1.keys())
        key2 = sorted(count2.keys())

        value1 = sorted(count1.values())
        value2 = sorted(count2.values())
        #print(key1,key2,value1,value2)
        return key1 == key2 and value1 == value2
        
        
        