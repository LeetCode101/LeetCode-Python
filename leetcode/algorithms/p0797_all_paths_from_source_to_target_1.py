from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        paths = []

        self._dfs(0, graph, [0], paths)

        return paths

    def _dfs(self, i, graph, path, paths):
        if i == len(graph) - 1:
            paths.append(path)
        else:
            for j in graph[i]:
                self._dfs(j, graph, path + [j], paths)
