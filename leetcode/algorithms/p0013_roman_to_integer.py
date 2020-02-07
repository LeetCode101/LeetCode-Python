class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'IV': 4,
            'X': 10,
            'IX': 9,
            'L': 50,
            'XL': 40,
            'C': 100,
            'XC': 90,
            'D': 500,
            'CD': 400,
            'M': 1000,
            'CM': 900
        }
        i, n = 0, len(s)
        count = 0

        while i < n:
            if i + 1 < n and romans.get(s[i] + s[i + 1], None):
                count += romans[s[i] + s[i + 1]]
                i += 2
            else:
                count += romans[s[i]]
                i += 1

        return count
