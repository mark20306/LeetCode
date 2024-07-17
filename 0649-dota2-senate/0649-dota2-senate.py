class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        d, r = deque(), deque()

        for i in range(n):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        while d and r:
            d_out = d.popleft()
            r_out = r.popleft()

            if d_out > r_out:
                r.append(r_out + n)
            else:
                d.append(d_out + n)
            
        return 'Radiant' if r else 'Dire'