from typing import List, Dict


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []

        self._search(letters, digits, 0, '', result)

        return result

    def _search(self, letters: Dict[str, str], digits: str,
                length: int, combination: str, result: List[str]):
        if length == len(digits):
            result.append(combination)

            return

        letter = digits[length]

        for c in letters[letter]:
            self._search(letters, digits, length + 1, combination + c, result)
