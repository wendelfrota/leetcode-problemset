import re


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub(r'\.', '[.]', address)


print(Solution().defangIPaddr('1.1.1.1'))
print(Solution().defangIPaddr('255.100.50.0'))
