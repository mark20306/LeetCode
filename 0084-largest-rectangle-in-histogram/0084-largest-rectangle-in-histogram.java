class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        Stack<int[]> stack = new Stack<>(); 

        for (int i = 0 ; i < heights.length ; i++){
            int start = i;
            while(!stack.isEmpty() && stack.peek()[1] > heights[i]){
                int[] top = stack.pop();
                int index = top[0];
                int height = top[1];
                maxArea = Math.max(maxArea , height * (i - index));
                start = index;
            }
            stack.push(new int[]{start , heights[i]});
        }
        for (int[] top : stack){
            int index = top[0];
            int height = top[1];
            maxArea = Math.max(maxArea , height * (heights.length - index));
        }
        return maxArea;
    }
}