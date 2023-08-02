class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table={} #創建hash表
        for i , num in enumerate(nums): 
        #使用 enumerate 函數來遍歷數組 nums，並獲取每個數值 num 和對應的索引 i
            result = target - num #使用target減去目前的num取得result        
            if result in hash_table :  #檢查result有無在hash表內          
                return [hash_table[result] , i] #有 直接返回 [hash_table[result], i]
            hash_table[num] = i #無 將 {num: i} 加入到hash表中            
        return [0,0] #如果整個遍歷結束仍然沒有找到符合條件的解，則返回 [0, 0]