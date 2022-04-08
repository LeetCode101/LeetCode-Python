import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = collections.defaultdict(int)

        for i, c in enumerate(order):
            order_map[c] = i

        chars = sorted(list(s), key=lambda x: order_map.get(x, len(order)))

        return ''.join(chars)
