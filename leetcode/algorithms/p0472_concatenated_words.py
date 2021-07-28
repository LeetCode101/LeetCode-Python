from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        result = []

        for word in words:
            if self._dfs(word, word_set):
                result.append(word)

        return result

    def _dfs(self, word, words):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in words and suffix in words:
                return True

            if prefix in words and self._dfs(suffix, words):
                return True

        return False
