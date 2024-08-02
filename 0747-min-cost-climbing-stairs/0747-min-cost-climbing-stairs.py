class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]
        
        first = cost[0]
        second = cost[1]
        for i in range(2, n):
            temp = cost[i] + min(first, second)
            first = second
            second = temp
        return min(first, second)