class Solution {
    public List<String> generateParenthesis(int n) {
        //不同於python解法
        List<String> res = new ArrayList<>();
        backtrack(res , "" , 0 , 0 , n);
        return res;
    }
    private void backtrack(List<String> res, String current, int openN , int closeN , int n){
        if(openN == n && closeN == n){
            //System.out.print(current);
            res.add(current);
            return;
        }
        if(openN < n){
            backtrack(res,current + "(",openN + 1,closeN,n);
        }
        if(closeN < openN){
            backtrack(res,current + ")",openN,closeN + 1,n);
        }
    }
}