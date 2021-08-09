class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(' ')
        words2 = sentence2.split(' ')
        i = j = 0

        if len(words1) > len(words2):
            words1, words2 = words2, words1

        while i < len(words1) and j < len(words2) and words1[i] == words2[j]:
            i += 1
            j += 1

        j = len(words2) - len(words1) + i

        while i < len(words1) and j < len(words2) and words1[i] == words2[j]:
            i += 1
            j += 1

        return i == len(words1) and j == len(words2)
