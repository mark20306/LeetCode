class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                prevNum = (i == 0 or flowerbed[i - 1] == 0)
                nextNum = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                if prevNum and nextNum:
                    flowerbed[i] = 1
                    n -= 1
        return n == 0
