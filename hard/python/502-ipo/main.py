import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        pq = []
        i = 0

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(pq, -projects[i][1])
                i += 1
            if not pq:
                break
            w -= heapq.heappop(pq)
        return w


# print(Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
# print(Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))
