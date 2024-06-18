class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for i in letters:
            if i>target:
                return i
        return letters[0]


print(Solution().nextGreatestLetter(['c', 'f', 'j'], 'a'))
print(Solution().nextGreatestLetter(['c', 'f', 'j'], 'c'))
print(Solution().nextGreatestLetter(['x', 'x', 'y', 'y'], 'z'))
