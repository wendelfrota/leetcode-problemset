from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        len_word = len(word)
        set_word = set(word)

        if len(set_word) == 1 or len(set_word) == len_word:
            return True

        freq = [0] * 26
        for i in word:
            freq[ord(i) - ord('a')] += 1

        count = Counter(freq)
        del count[0]

        if len(count) != 2:
            return False

        key_min, key_max = min(count.keys()), max(count.keys())

        if key_min == count[key_min] == 1:
            return True

        return True if key_max - key_min == 1 and count[key_max] == 1 else False


# print(Solution().equalFrequency('abcc'))
# print(Solution().equalFrequency('aazz'))
# print(Solution().equalFrequency('ddaccb'))
# print(Solution().equalFrequency('aca'))
# print(Solution().equalFrequency('cbccca'))
