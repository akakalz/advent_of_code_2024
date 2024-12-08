class FourPointShape:
    def __init__(self, p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int], p4: tuple[int, int]) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def is_rectangle(self) -> bool:
        return any([
            self._is_rectangle_unordered(self.p1, self.p2, self.p3, self.p4),
            self._is_rectangle_unordered(self.p2, self.p3, self.p1, self.p4),
            self._is_rectangle_unordered(self.p3, self.p1, self.p2, self.p4),
        ])

    def _is_orthogonal(self, p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]) -> bool:
        return (p2[0] - p1[0]) * (p2[0] - p3[0]) + (p2[1] - p1[1]) * (p2[1] - p3[1]) == 0

    def _is_rectangle_unordered(
            self,
            p1: tuple[int, int],
            p2: tuple[int, int],
            p3: tuple[int, int],
            p4: tuple[int, int],
        ) -> bool:
        return all([
            self._is_orthogonal(p1, p2, p3),
            self._is_orthogonal(p2, p3, p4),
            self._is_orthogonal(p3, p4, p1),
        ])
