from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str],
                      score: List[int]) -> int:
        counts = [0] * 26

        for c in letters:
            counts[ord(c) - 97] += 1

        return self._search(words, 0, counts, score)

    def _search(self, words, start, counts, scores):
        max_score = 0

        for i in range(start, len(words)):
            score = 0
            is_valid = True

            for c in words[i]:
                counts[ord(c) - 97] -= 1
                score += scores[ord(c) - 97]

                if counts[ord(c) - 97] < 0:
                    is_valid = False

            if is_valid:
                score += self._search(words, i + 1, counts, scores)
                max_score = max(max_score, score)

            for c in words[i]:
                counts[ord(c) - 97] += 1

        return max_score
