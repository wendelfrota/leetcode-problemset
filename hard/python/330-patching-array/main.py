class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        miss, i, added = 1, 0, 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1

        return added


# print(Solution().minPatches([1, 3], 6))
# print(Solution().minPatches([1, 5, 10], 20))
# print(Solution().minPatches([1, 2, 2], 5))
