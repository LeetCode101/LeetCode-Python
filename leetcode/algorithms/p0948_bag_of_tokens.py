from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        low, high = 0, len(tokens) - 1
        sorted_tokens = sorted(tokens)

        while low <= high:
            if power >= sorted_tokens[low]:
                power -= sorted_tokens[low]
                score += 1
                low += 1
            elif score > 0 and low != high:
                power += sorted_tokens[high]
                score -= 1
                high -= 1
            else:
                break

        return score
