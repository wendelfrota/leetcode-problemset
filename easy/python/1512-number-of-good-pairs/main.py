import collections
import math


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum([math.comb(n, 2) for n in collections.Counter(nums).values()])


# print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
# print(Solution().numIdenticalPairs([1, 1, 1, 1]))
# print(Solution().numIdenticalPairs([1, 2, 3]))
