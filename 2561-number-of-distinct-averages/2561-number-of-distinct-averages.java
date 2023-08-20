class Solution {
    public int distinctAverages(int[] nums) {
        Arrays.sort(nums);
        List<Double> res = new ArrayList<>();
        int l = 0 , r = nums.length - 1;
        while(l < r){
            double num = (double) (nums[l] + nums[r]) / 2;
            //System.out.print(num);
            if(!res.contains(num)){
                res.add(num);
            }
            l++;
            r--;
        }
        return res.size();
    }
}