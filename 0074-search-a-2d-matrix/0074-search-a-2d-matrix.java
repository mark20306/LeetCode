class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length , cols = matrix[0].length;
        int top = 0 , bot = rows - 1;

        while(top <= bot){
            int row = (top + bot) / 2;
            if(target > matrix[row][cols - 1]){
                top = row + 1;
            }else if(target < matrix[row][0]){
                bot = row - 1;
            }else{
                break;
            }
        }
        if(!(top <= bot)){
            return false;
        }
        int l = 0 , r = cols - 1;
        int row = (top + bot) / 2;
        while(l <= r){
            int m = (l + r) / 2;
            if(target == matrix[row][m]){
                return true;
            }else if(target > matrix[row][m]){
                l = m + 1;
            }else{
                r = m - 1;
            }
        }
        return false;
    }
}