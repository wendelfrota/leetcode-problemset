from functools import reduce


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return reduce(lambda x, y: x + [nums[y], nums[y + n]], range(n), [])


print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3))
print(Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
print(Solution().shuffle([1, 1, 2, 2], 2))
