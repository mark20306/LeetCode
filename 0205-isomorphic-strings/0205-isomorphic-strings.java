class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character,Character> hashmap = new HashMap<>();
        for(int i=0;i<s.length();i++){
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            
            if(hashmap.containsKey(sChar)){
                if(tChar != hashmap.get(sChar)){
                    return false;
                }
            }else{
                if(hashmap.containsValue(tChar)){
                    return false;
                }else{
                    hashmap.put(sChar,tChar);
                }
            }
        }
        return true;
        
    }
} 





