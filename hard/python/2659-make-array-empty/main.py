class Solution:
    def countOperationsToEmptyArray(self, nums: list[int]) -> int:
        n, res, turn = len(nums), 1, 1
        idx = sorted(range(n), key=lambda x: nums[x])
        for i in range(1, n):
            turn += idx[i] < idx[i-1]
            res += turn
        return res


# print(Solution().countOperationsToEmptyArray([3, 4, -1]))
# print(Solution().countOperationsToEmptyArray([1, 2, 4, 3]))
# print(Solution().countOperationsToEmptyArray([1, 2, 3]))
