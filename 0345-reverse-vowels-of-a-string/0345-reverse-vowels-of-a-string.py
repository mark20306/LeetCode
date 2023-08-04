class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowels_index = [n for n in range(len(s)) if s[n] in vowels]
        v = list(s)        
        i , j = 0 , len(vowels_index) - 1
        while i < j:
            v[vowels_index[i]] , v[vowels_index[j]] = v[vowels_index[j]] , v[vowels_index[i]]
            i += 1
            j -= 1
        return "".join(v)    
