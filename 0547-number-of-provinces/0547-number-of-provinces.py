class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for j in range(len(isConnected)):
                if isConnected[city][j] == 1 and not visit[j]:
                    visit[j] = True
                    dfs(j)

        visit = [False] * len(isConnected)
        ans = 0
        for i in range(len(isConnected)):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                ans += 1

        return ans
        