class Solution:
    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1

        while low < high:
            if not self._is_valid_letter(s[low]):
                low += 1
            elif not self._is_valid_letter(s[high]):
                high -= 1
            elif s[low].lower() != s[high].lower():
                return False
            else:
                low += 1
                high -= 1

        return True

    def _is_valid_letter(self, s: str) -> bool:
        return 'a' <= s <= 'z' or 'A' <= s <= 'Z' or '0' <= s <= '9'
