class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        int low = prices[0];
        for(int price : prices){
            if(low > price){
                low = price;
            }
            res = Math.max(res , price - low);
        }
        return res;
    }
}