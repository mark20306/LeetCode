class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            n -= 1
            if n <= 0:
                return True
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0:
                if flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1 and flowerbed[i] == 0:
                if flowerbed[i - 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            if n <= 0:
                return True
        return False