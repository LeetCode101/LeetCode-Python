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
        roots = {mail: mail for mail in mails}

        for account in accounts:
            for i in range(2, len(account)):
                self._union(roots, account[i - 1], account[i])

        components = collections.defaultdict(list)

        for mail in roots.keys():
            root = self._get_root(roots, mail)
            components[root].append(mail)

        for root, mails in components.items():
            person = mail_to_person[root]
            result.append([person] + sorted(mails))

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
