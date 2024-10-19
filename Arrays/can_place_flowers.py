class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            previous_flowerbed = i == 0 or flowerbed[i-1] == 0
            next_flowerbed = i == len(flowerbed) - 1 or flowerbed[i+1] == 0
            if previous_flowerbed and next_flowerbed and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0