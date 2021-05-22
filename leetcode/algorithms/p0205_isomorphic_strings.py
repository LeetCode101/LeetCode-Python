class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t = {}
        t2s = {}

        for i, c in enumerate(s):
            if c not in s2t and t[i] not in t2s:
                s2t[c] = t[i]
                t2s[t[i]] = c
            elif s2t.get(c, '') != t[i] and t2s.get(t[i], '') != c:
                return False

        return True
