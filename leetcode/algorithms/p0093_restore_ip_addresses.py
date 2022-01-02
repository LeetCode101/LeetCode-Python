from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        self._restore(s, [], result)

        return list(map(lambda x: '.'.join(x), result))

    def _restore(self, s, ip_so_far, result):
        if not s:
            if len(ip_so_far) == 4:
                result.append(ip_so_far)

            return

        if len(ip_so_far) == 4:
            return

        n = len(s)

        self._restore(s[1:], ip_so_far + [s[0]], result)

        if s[0] != '0':
            if n >= 2:
                self._restore(s[2:], ip_so_far + [s[0:2]], result)

            if n >= 3 and int(s[0:3]) <= 255:
                self._restore(s[3:], ip_so_far + [s[0:3]], result)
