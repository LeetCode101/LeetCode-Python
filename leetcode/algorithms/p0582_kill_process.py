import collections
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) \
            -> List[int]:
        parent_to_children = collections.defaultdict(list)

        for i, id in enumerate(pid):
            parent_to_children[ppid[i]].append(id)

        processes = [kill]
        queue = collections.deque(parent_to_children[kill])

        while queue:
            process = queue.popleft()

            processes.append(process)

            if parent_to_children[process]:
                for child in parent_to_children[process]:
                    queue.append(child)

        return processes
