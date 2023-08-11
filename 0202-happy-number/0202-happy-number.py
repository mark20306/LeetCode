
class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(n:int) -> int:
            currentNum = 0
            while n > 0:
                digit = n % 10
                currentNum += digit ** 2
                n //= 10
            return currentNum
        '''slow = fast = n
        while True:
            slow = squareSum(slow)
            fast = squareSum(squareSum(fast))
            if slow == fast:
                break
        return slow == 1'''
        visit = set()
        while n not in visit:
            visit.add(n)
            n = squareSum(n)
            if n == 1:
                return True
        