import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mails = []
        result = []
        mail_to_person = {}

        for account in accounts:
            for i in range(1, len(account)):
                mails.append(account[i])
                mail_to_person[account[i]] = account[0]

        mail_to_number = {mails[i]: i for i in range(len(mails))}
        number_to_mail = {i: mails[i] for i in range(len(mails))}
        roots = list(range(len(mails)))

        for account in accounts:
            for i in range(2, len(account)):
                a = mail_to_number[account[i - 1]]
                b = mail_to_number[account[i]]

                self._union(roots, a, b)

        components = collections.defaultdict(list)

        for root in roots:
            components[self._get_root(roots, root)].append(root)

        for root, nodes in components.items():
            mails = sorted([number_to_mail[i] for i in nodes])
            person = mail_to_person[number_to_mail[root]]
            result.append([person] + mails)

        return result

    def _get_root(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x

    def _union(self, roots, a, b):
        root_a = self._get_root(roots, a)
        root_b = self._get_root(roots, b)

        roots[root_a] = root_b
