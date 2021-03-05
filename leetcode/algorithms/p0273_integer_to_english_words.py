import math


class Solution:
    def __init__(self):
        self.less_than_10 = {
            '0': 'Zero',
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine'
        }
        self.less_than_20 = {
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen'
        }
        self.larger_than_20 = {
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '6': 'Sixty',
            '7': 'Seventy',
            '8': 'Eighty',
            '9': 'Ninety'
        }

    def numberToWords(self, num: int) -> str:
        number_string = str(num)
        length = len(number_string)
        i = 0
        words = []
        separators = {
            1: '',
            2: 'Thousand',
            3: 'Million',
            4: 'Billion'
        }

        while i < length:
            high_digits_length = (length - i) % 3
            separator = separators.get(math.ceil((length - i) / 3), '')
            high_digits = number_string[i:i + high_digits_length] \
                if high_digits_length != 0 else number_string[i:i + 3]
            digits = self._trim_zero(high_digits)
            word = ''

            if len(digits) == 3:
                word = self._parse_three_digits(digits)
            elif len(digits) == 2:
                word = self._parse_two_digits(digits)
            elif len(digits) == 1:
                word = self._parse_one_digit(digits)

            if word:
                words.append(word + (' ' + separator if separator else ''))

            i += len(high_digits)

        return ' '.join(words)

    def _parse_three_digits(self, num: str) -> str:
        left = int(num[1:])

        return self._parse_one_digit(num[0]) + ' Hundred' + \
            (' ' + self._parse_two_digits(str(left)) if left != 0 else '')

    def _parse_two_digits(self, num: str) -> str:
        if len(num) == 1:
            return self._parse_one_digit(num)
        elif int(num) < 20:
            return self.less_than_20[num]
        elif num[1] == '0':
            return self.larger_than_20[num[0]]
        else:
            return self.larger_than_20[num[0]] + ' ' + \
                   self.less_than_10[num[1]]

    def _parse_one_digit(self, num: str) -> str:
        return self.less_than_10[num]

    def _trim_zero(self, num: str) -> str:
        if len(num) == 1:
            return num

        i = 0

        while i < len(num) and num[i] == '0':
            i += 1

        return num[i:]
