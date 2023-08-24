class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double maxnum = Double.NEGATIVE_INFINITY;
        double temp = 0;
        for(int i = 0; i < nums.length; i++){
            temp  += nums[i];
            if(i >= k){
                temp -= nums[i - k];
            }
            if(i >= k-1){
                maxnum = Math.max(maxnum , temp);
            }
        }
        return maxnum / k;
    }
}