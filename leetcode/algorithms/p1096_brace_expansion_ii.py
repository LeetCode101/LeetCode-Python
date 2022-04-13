from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack, union, product = [], [], ['']

        for c in expression:
            if c.isalpha():
                product = [r + c for r in product]
            elif c == '{':
                stack.append(union)
                stack.append(product)
                union, product = [], ['']
            elif c == '}':
                pre_product, pre_union = stack.pop(), stack.pop()
                product = [p + r for r in product + union for p in pre_product]
                union = pre_union
            elif c == ',':
                union += product
                product = ['']

        return sorted(set(union + product))
