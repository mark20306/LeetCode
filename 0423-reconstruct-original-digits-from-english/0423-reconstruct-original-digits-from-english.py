class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        num = [0] * 10
        
        num[0] = c["z"] # "zero" 中唯一的 'z'
        num[2] = c["w"] # "two" 中唯一的 'w'
        num[4] = c["u"] # "four" 中唯一的 'u'
        num[6] = c["x"] # "six" 中唯一的 'x'
        num[8] = c["g"] # "eight" 中唯一的 'g'

        num[3] = c["h"] - num[8] # "three" 中的 'h'，但需要扣除 "eight" 中的 'h'
        num[5] = c["f"] - num[4] # "five" 中的 'f'，但需要扣除 "four" 中的 'f'
        num[7] = c["s"] - num[6] # "seven" 中的 's'，但需要扣除 "six" 中的 's'
        num[1] = c["o"] - num[0] - num[2] - num[4] # "one" 中的 'o'，需要扣除 "zero"、"two" 和 "four" 中的 'o'
        num[9] = c["i"] - num[5] - num[6] - num[8] # "nine" 中的 'i'，需要扣除 "five"、"six" 和 "eight" 中的 'i'

        ans = []
        for i in range(10):
            ans.append(str(i) * num[i])
        return "".join(ans)