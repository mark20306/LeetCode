class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            elif i == 20:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True