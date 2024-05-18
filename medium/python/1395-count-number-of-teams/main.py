from sortedcontainers import SortedList


class Solution:
    def count(self, sorted_list, value):
        less = sorted_list.bisect_left(value)
        greater = len(sorted_list) - less
        return less, greater

    def numTeams(self, rating: list[int]) -> int:
        total_teams = 0

        left_list = SortedList()
        right_list = SortedList(rating)

        for i in rating:
            right_list.remove(i)

            less_left, greater_left = self.count(left_list, i)
            less_right, greater_right = self.count(right_list, i)

            total_teams += less_left * greater_right + greater_left * less_right

            left_list.add(i)

        return total_teams


# print(Solution().numTeams([2, 5, 3, 4, 1]))
