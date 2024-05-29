class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) + int(coordinates[1])) & 1


# print(Solution().squareIsWhite('a1'))
# print(Solution().squareIsWhite('b2'))
# print(Solution().squareIsWhite('h3'))
# print(Solution().squareIsWhite('c7'))
