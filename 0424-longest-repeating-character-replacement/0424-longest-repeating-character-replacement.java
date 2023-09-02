class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;
        HashMap<Character , Integer> count = new HashMap<>();
        int l = 0;
        int maxf = 0;
        for(int r = 0 ; r < s.length() ; r++){
            count.put(s.charAt(r) , count.getOrDefault(s.charAt(r) , 0) + 1);
            maxf = Math.max(maxf , count.get(s.charAt(r)));
            while((r - l + 1) - maxf > k){
                count.put(s.charAt(l) , count.get(s.charAt(l)) - 1);
                l += 1;
            } 
            res = Math.max(res , r - l + 1);
        }
        return res;
    }
}