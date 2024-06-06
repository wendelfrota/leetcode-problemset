class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        i = 0
        jewels = sorted(jewels)

        for jewel in jewels:
            if jewel in stones:
                i += stones.count(jewel)
        return i


# print(Solution().numJewelsInStones("aA", "aAAbbbb"))
# print(Solution().numJewelsInStones("z", "ZZ"))
