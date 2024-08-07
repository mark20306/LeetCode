class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        

        below_20 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        thousands = ['','Thousand','Million','Billion']

        def word(n):
            if n == 0:
                return ''
            elif n < 20:
                return below_20[n] + ' '
            elif n < 100:
                return tens[n // 10] + ' ' + word(n % 10)
            else:
                return below_20[n // 100] + ' Hundred ' + word(n % 100)
            
        ans = ''

        for i in range(len(thousands)):
            if num % 1000 != 0:
                ans = word(num % 1000) + thousands[i] + ' ' + ans
            num //= 1000
        return ans.strip()

            
