class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        for(int i : nums1){
            int l = 0 , r = nums2.length - 1;
            while(l <= r){
                int mid = (r - l) / 2 + l;
                if(i == nums2[mid]){
                    return i;
                }else if(i < nums2[mid]){
                    r = mid - 1;
                }else{
                    l = mid + 1;
                }
            }
        }
        return -1;
    }
}