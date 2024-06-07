from heapq import heappop, heappush


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pq = []
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if len(pq) < ladders:
                    heappush(pq, diff)
                else:
                    if not pq or pq[0] >= diff:
                        bricks -= diff
                    else:
                        poll = heappop(pq)
                        heappush(pq, diff)
                        bricks -= poll
                    if bricks < 0:
                        return i
        return n-1


# print(Solution().furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
# print(Solution().furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))
# print(Solution().furthestBuilding([14, 3, 19, 3], 17, 0))
