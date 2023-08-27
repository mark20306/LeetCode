class Solution {
    public int search(int[] nums, int target) {
        int l = 0 , r = nums.length - 1;
        while(l <= r){
            int m = (r -l) / 2 + l;
            if(target == nums[m]){
                return m;
            }
            if(nums[m] >= nums[l]){
                if(target < nums[l] || target > nums[m] ){
                    l = m + 1;
                }else{
                    r = m - 1;
                }
            }else{
                if(target > nums[r] || target < nums[m]){
                    r = m - 1;
                }else{
                    l = m + 1;
                }
            }
        }
        return -1;
    }
}