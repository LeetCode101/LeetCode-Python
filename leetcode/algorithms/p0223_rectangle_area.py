class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int,
                    E: int, F: int, G: int, H: int) -> int:
        area1 = abs((C - A) * (D - B))
        area2 = abs((G - E) * (H - F))
        overlap_area = 0 if self._is_overlap(A, B, C, D, E, F, G, H) \
            else (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))

        return area1 + area2 - overlap_area

    def _is_overlap(self, A: int, B: int, C: int, D: int,
                    E: int, F: int, G: int, H: int) -> bool:
        return E >= C or A >= G or B >= H or D <= F
