import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mails = set()
        result = []
        mail_to_person = {}

        for account in accounts:
            for i in range(1, len(account)):
                mail = account[i]
                mails.add(mail)
                mail_to_person[mail] = account[0]

        mails = list(mails)
        n = len(mails)
        mail_to_number = {mails[i]: i for i in range(n)}
        number_to_mail = {i: mails[i] for i in range(n)}
        roots = list(range(n))

        for account in accounts:
            for i in range(2, len(account)):
                a = mail_to_number[account[i - 1]]
                b = mail_to_number[account[i]]

                self._union(roots, a, b)

        components = collections.defaultdict(list)

        for i, root in enumerate(roots):
            components[self._get_root(roots, root)].append(i)

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
