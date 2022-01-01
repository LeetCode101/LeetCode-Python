class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self._match(pattern, s, {})

    def _match(self, pattern, s, mapping):
        if not pattern:
            return not s
        elif pattern[0] in mapping:
            matched = mapping[pattern[0]]

            if s[:len(matched)] != matched:
                return False

            if self._match(pattern[1:], s[len(matched):], mapping):
                return True
        else:
            for i in range(1, len(s) + 1):
                candidate = s[:i]

                if candidate in mapping.values():
                    continue

                mapping[pattern[0]] = candidate

                if self._match(pattern[1:], s[i:], mapping):
                    return True

                mapping.pop(pattern[0])

        return False
