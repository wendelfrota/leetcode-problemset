from heapq import heappushpop, heappush


class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        pq = []
        s = 0
        ans = 0

        for duration, last in courses:
            if last < duration: continue
            if s + duration <= last:
                heappush(pq, -duration)
                s += duration
                ans += 1
            else:
                if -pq[0] <= duration: continue
                s += duration + heappushpop(pq, -duration)
        return ans


# print(Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
# print(Solution().scheduleCourse([[1, 2]]))
# print(Solution().scheduleCourse([[3, 2], [4, 3]]))
