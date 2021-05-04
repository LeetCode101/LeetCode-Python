from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''

        if len(strs) < 1:
            return ''
        elif len(strs) == 1:
            return strs[0]

        for i, c in enumerate(strs[0]):
            is_common = True

            for text in strs:
                is_common = text and i < len(text) and text[i] == c

                if not is_common:
                    break

            if is_common:
                common += c
            else:
                break

        return common
