class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 2):
            if (arr[i] & 1) and (arr[i + 1] & 1) and (arr[i + 2] & 1):
                return True
        return False


# print(Solution().threeConsecutiveOdds([2, 6, 4, 1]))
# print(Solution().threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
