import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph, visited, result = collections.defaultdict(list), set(), []

        for account in accounts:
            for i in range(2, len(account)):
                graph[account[i]].append(account[i - 1])
                graph[account[i - 1]].append(account[i])

        for account in accounts:
            if account[1] not in visited:
                result.append([account[0]] +
                              sorted(self._dfs(account[1], graph, visited)))

        return result

    def _dfs(self, email, graph, visited):
        visited.add(email)
        emails = [email]

        for neighbour in graph[email]:
            if neighbour not in visited:
                emails.extend(self._dfs(neighbour, graph, visited))

        return emails
