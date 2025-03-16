class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $res = [];
        foreach($nums as $i => $num){
            $temp = $target - $num;
            if(isset($res[$temp])){
                return [$res[$temp], $i];
            }
            $res[$num] = $i;
        }
        return [];
    }
}