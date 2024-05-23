class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort(reverse=True)

        count = res = 0

        for i in satisfaction:
            if i + count < 0:
                return res

            count += i
            res += count

        return res


# print(Solution().maxSatisfaction([-1, -8, 0, 5, -9]))
# print(Solution().maxSatisfaction([4, 3, 2]))
# print(Solution().maxSatisfaction([-1, -4, -5]))

