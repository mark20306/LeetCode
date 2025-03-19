class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry < 10:
                digits[i] += 1
                return digits
            digits[i] = 0
            carry = 1
        return [1] + digits