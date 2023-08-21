class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Stack<Integer> stack = new Stack<>();

        for(int curr = 0; curr < temperatures.length ; curr++){
            while(!stack.isEmpty() && temperatures[curr] > temperatures[stack.peek()]){
                int prev = stack.pop();
                res[prev] = curr - prev;
            }
            stack.add(curr);
        }
        return res;
    }
}