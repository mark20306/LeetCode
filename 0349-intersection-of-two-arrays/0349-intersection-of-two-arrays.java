class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        List<Integer> res = new ArrayList<>();
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        for(int i : nums1){
            int l = 0;
            int r = nums2.length - 1;
            while(l <= r){
                int mid = (l + r) / 2;
                if(nums2[mid] == i && !res.contains(i)){
                    res.add(i);
                }else if(nums2[mid] > i){
                    r = mid - 1;
                }else{
                    l = mid + 1;
                }
            }
        }
        int[] result = new int[res.size()];
        for(int i = 0 ; i < res.size() ; i++){
            result[i] = res.get(i);
        }
        return result;
    }
}