class Solution {
    public int maxDepth(String s) {
        int count = 0;
        int res = 0;
        for(char i : s.toCharArray()){
            if(i == '('){
                count += 1;
                res = Math.max(res , count);
            }
            if(i == ')'){
                count -= 1;
            }
        }
        return res;
    }
}