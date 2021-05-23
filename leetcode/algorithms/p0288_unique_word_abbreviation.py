from typing import List


class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        abbreviations = {}

        for word in dictionary:
            abbreviation = self._get_abbreviation(word)

            if abbreviation in abbreviations:
                abbreviations[abbreviation].add(word)
            else:
                abbreviations[abbreviation] = {word}

        self.abbreviations = abbreviations

    def isUnique(self, word: str) -> bool:
        abbreviation = self._get_abbreviation(word)

        if abbreviation not in self.abbreviations:
            return True
        elif word in self.abbreviations[abbreviation] \
                and len(self.abbreviations[abbreviation]) == 1:
            return True
        else:
            return False

    def _get_abbreviation(self, word):
        if len(word) <= 2:
            return word

        return word[0] + str(len(word) - 2) + word[-1]
