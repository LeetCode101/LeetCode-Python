import collections
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) \
            -> List[int]:
        parent_to_children = collections.defaultdict(list)

        for i, id in enumerate(pid):
            parent_to_children[ppid[i]].append(id)

        processes = []
        stack = [kill]

        while stack:
            process = stack.pop()
            processes.append(process)

            for child in parent_to_children[process]:
                stack.append(child)

        return processes
