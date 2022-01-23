
class Solution:
    # Using Loop
    # Time complexity n space complexity 1
    
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 else False

        for i in range(len(flowerbed)):
            if n == 0:
                return True

            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

            elif flowerbed[i] == 0 and i == len(flowerbed)-1 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

        if n == 0:
            return True
        return False


sol = Solution()

print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 1))
