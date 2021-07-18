import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counter = collections.Counter(words)
        word_length = len(words[0])
        positions = []

        for start in range(len(s) - len(words) * word_length + 1):
            current_counter = collections.defaultdict(int)

            for i in range(len(words)):
                word_start, word_end = start + i * word_length, \
                                       start + (i + 1) * word_length
                word = s[word_start:word_end]
                current_counter[word] += 1

                if word not in counter:
                    break

                if current_counter[word] > counter[word]:
                    break

            if current_counter == counter:
                positions.append(start)

        return positions
