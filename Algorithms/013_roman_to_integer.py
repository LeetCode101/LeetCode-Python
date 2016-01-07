#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def romanToInt(self, s):
        r = re.compile('(M*)(CD|CM|D{0,1}C{0,3})(XL|XC|L{0,1}X{0,3})(IV|IX|V{0,1}I{0,3})')
        match = r.search(s)
        group, current_group = match.groups(), ''
        p, integer = 0, 0
        symbol = {}
        symbols = [
            {
                'symbol': 'I',
                'symbol_for_five': 'V',
                'symbol_for_ten': 'X'
            },
            {
                'symbol': 'X',
                'symbol_for_five': 'L',
                'symbol_for_ten': 'C'
            },
            {
                'symbol': 'C',
                'symbol_for_five': 'D',
                'symbol_for_ten': 'M'
            },
            {
                'symbol': 'M',
                'symbol_for_five': 'Undefined',
                'symbol_for_ten': 'Undefined'
            }
        ]
        
        for i in range(0, len(group)):
            p = pow(10, 4 - i - 1)
            current_group, symbol = group[i], symbols[4 - i - 1]
            
            if current_group == '':
                continue
            
            if current_group == symbol['symbol'] + symbol['symbol_for_five']:
                integer += 4 * p
            elif current_group == symbol['symbol'] + symbol['symbol_for_ten']:
                integer += 9 * p
            else:
                integer += current_group.count(symbol['symbol_for_five']) * p * 5 + current_group.count(symbol['symbol']) * p
        
        return integer
