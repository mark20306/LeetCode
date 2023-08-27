class Solution {
    public int longestAlternatingSubarray(int[] nums, int threshold) {
        int res = 0;
        int curr = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0 && nums[i] <= threshold) {
                curr = 1;
                res = Math.max(res, curr);
                while (i + 1 < nums.length && nums[i] % 2 != nums[i + 1] % 2 && nums[i+1] <= threshold) {
                    curr++;
                    res = Math.max(res, curr);
                    i++;
                }
            } else {
                curr = 0;
            }
        }
        return res;
    }
}