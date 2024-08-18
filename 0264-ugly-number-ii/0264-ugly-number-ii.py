class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = []
        minheap = [1]
        while minheap and len(ans) < n:
            num = heapq.heappop(minheap)
            if num not in ans:
                ans.append(num)
                heapq.heappush(minheap, num * 2)
                heapq.heappush(minheap, num * 3)
                heapq.heappush(minheap, num * 5)
        return ans[-1]