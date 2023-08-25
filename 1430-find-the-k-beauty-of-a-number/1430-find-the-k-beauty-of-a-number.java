class Solution {
    public int divisorSubstrings(int num, int k) {
        int res = 0;
        String numstr = String.valueOf(num);
        for(int i = 0 ; i <= numstr.length() - k  ; i++){
            int n = Integer.parseInt(numstr.substring(i , i+k));
            if(n !=  0 && num % n == 0){
                res += 1;
            }
        }
        return res;
    }
}