class Solution:
    def findNthDigit(self, n: int) -> int:
        dpn = 1
        count = 9
        while dpn * count < n:
            n -= dpn * count
            dpn += 1
            count *= 10

        number = 10 ** (dpn - 1) + (n - 1) // dpn
        return int(str(number)[(n - 1) % dpn])


# print(Solution().findNthDigit(3))
# print(Solution().findNthDigit(11))
