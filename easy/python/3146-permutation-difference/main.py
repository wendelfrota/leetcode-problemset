class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0

        for i in range(len(s)):
            res += abs(s.index(s[i]) - t.index(s[i]))

        return res


# print(Solution().findPermutationDifference('abc', 'bac'))
# print(Solution().findPermutationDifference('abcde', 'edbac'))
