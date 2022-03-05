import collections


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self._max_consecutive(answerKey, 'T', k),
                   self._max_consecutive(answerKey, 'F', k))

    def _max_consecutive(self, answer_key, target, k):
        max_length = 0
        counter = collections.defaultdict(int)
        start = 0

        for end, c in enumerate(answer_key):
            counter[c] += 1

            while start <= end and counter[target] > k:
                counter[answer_key[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
