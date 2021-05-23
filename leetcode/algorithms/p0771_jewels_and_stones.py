class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(list(jewels))
        count = 0

        for stone in stones:
            if stone in jewels_set:
                count += 1

        return count
