class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        currStr = ''
        currCount = 0

        for i in s:
            if i.isdigit():
                currCount = currCount * 10 + int(i)
            elif i == '[':
                countStack.append(currCount)
                stringStack.append(currStr)
                currStr = ''
                currCount = 0
            elif i == ']':
                repeatTimes = countStack.pop()
                prevString = repeatTimes * currStr
                currStr =stringStack.pop() +  prevString 
            else:
                currStr += i
        return currStr