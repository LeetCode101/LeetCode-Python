#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        i = 0
        result = []
        words_in_line = []
        words_in_line_length = 0
        words_length = len(words)
            
        while i < words_length:
            current_word_length = len(words[i])
            
            if words_in_line_length + current_word_length + 1 <= maxWidth or words_in_line_length + current_word_length <= maxWidth:
                words_in_line.append(words[i])
                
                i += 1
                words_in_line_length += current_word_length + 1
            else:
                is_last_line = i == words_length
                extra_spaces_length = maxWidth - (words_in_line_length - 1)
                
                result.append(self.create_line(words_in_line, extra_spaces_length, is_last_line))
                
                words_in_line = []
                words_in_line_length = 0

        if len(words_in_line) > 0:
            result.append(self.create_line(words_in_line, maxWidth - (words_in_line_length - 1), True))
            
        return result
    
    def create_line(self, words, extra_spaces_length, is_last_line):
        line = ''
        words_length = len(words)
        spaces_between_words = [1] * (words_length - 1)
        
        if extra_spaces_length == 0:
            return ' '.join(words)
        
        if words_length == 1:
            return words[0] + ' ' * extra_spaces_length
        
        if is_last_line:
            return ' '.join(words) + ' ' * extra_spaces_length

        while extra_spaces_length != 0:
            for i in range(words_length - 1):
                if extra_spaces_length > 0:
                    spaces_between_words[i] += 1
                    extra_spaces_length -= 1
                else:
                    break
        
        if extra_spaces_length > 0:
            spaces_between_words[0] += extra_spaces_length
        
        for i in range(words_length):
            if i < words_length - 1:
                line += words[i] + spaces_between_words[i] * ' '
            else:
                line+= words[i]
        
        return line
