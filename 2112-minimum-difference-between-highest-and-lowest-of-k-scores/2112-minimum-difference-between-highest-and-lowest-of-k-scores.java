class Solution {
    public int minimumDifference(int[] nums, int k) {
        if(nums.length <= 1){
            return 0;
        }
        int res =Integer.MAX_VALUE; 
        int l = 0;
        Arrays.sort(nums);
        for(int r = k - 1 ; r < nums.length ; r++){
            res = Math.min(res , nums[r] - nums[l]);
            l += 1;
        }
        return res;
    }
}