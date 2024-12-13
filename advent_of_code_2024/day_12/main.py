from dataclasses import dataclass
from advent_of_code_2024.day import Day


UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
UP_RIGHT = (1, -1)
DOWN_RIGHT = (1, 1)
DOWN_LEFT = (-1, 1)
UP_LEFT = (-1, -1)


@dataclass
class CornerChecker:
    dir_in_region: list[tuple[tuple[int, int], bool]]
    corners: int


class Day12(Day):
    def __init__(self):
        super().__init__(12, f"advent_of_code_2024/day_12/puzzle_input.txt")
        self._x_bound = len(self.input_data[0])
        self._y_bound = len(self.input_data)
        self.directions = (UP, RIGHT, DOWN, LEFT)

    def _on_map(self, pos: tuple[int, int]) -> bool:
        return all([
            0 <= pos[0] < self._x_bound,
            0 <= pos[1] < self._y_bound,
        ])

    def tup_add(self, t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    def _setup_region(self, label: str, start_pos: tuple[int, int], total_visited: set) -> dict:
        region = {}
        self._setup_helper(label, start_pos, region, total_visited)
        return region

    def _setup_helper(self, label: str, cur_pos: tuple[int, int], region: dict, total_visited: set) -> None:
        total_visited.add(cur_pos)
        region[cur_pos] = set()
        for d in self.directions:
            nc, nr = self.tup_add(cur_pos, d)
            if not self._on_map((nc, nr)):
                continue
            if self.input_data[nr][nc] == label:
                region[cur_pos].add((nc, nr))
                if (nc, nr) not in total_visited:
                    self._setup_helper(label, (nc, nr), region, total_visited)

    def _count_corners(self, region: dict[tuple[int, int], set[tuple[int, int]]]) -> int:
        corner_possibles = (
            # all four corners (single member region)
            CornerChecker(
                dir_in_region=[(UP, False), (RIGHT, False), (DOWN, False), (LEFT, False)],
                corners=4,
            ),
            # two corners (penisula)
            CornerChecker(
                dir_in_region=[(UP, False), (RIGHT, False), (DOWN, False), (LEFT, True)],
                corners=2,
            ),
            CornerChecker(
                dir_in_region=[(UP, False), (RIGHT, False), (DOWN, True), (LEFT, False)],
                corners=2,
            ),
            CornerChecker(
                dir_in_region=[(UP, False), (RIGHT, True), (DOWN, False), (LEFT, False)],
                corners=2,
            ),
            CornerChecker(
                dir_in_region=[(UP, True), (RIGHT, False), (DOWN, False), (LEFT, False)],
                corners=2,
            ),
            # 1 corner, outer
            CornerChecker(
                dir_in_region=[(UP, False), (RIGHT, True), (DOWN, True), (LEFT, False)],
                corners=1,
            ),
            CornerChecker(
                dir_in_region=[(UP, False), (RIGHT, False), (DOWN, True), (LEFT, True)],
                corners=1,
            ),
            CornerChecker(
                dir_in_region=[(UP, True), (RIGHT, False), (DOWN, False), (LEFT, True)],
                corners=1,
            ),
            CornerChecker(
                dir_in_region=[(UP, True), (RIGHT, True), (DOWN, False), (LEFT, False)],
                corners=1,
            ),
            # 1 corner, inner
            CornerChecker(
                dir_in_region=[(UP, True), (RIGHT, True), (UP_RIGHT, False)],
                corners=1,
            ),
            CornerChecker(
                dir_in_region=[(UP, True), (LEFT, True), (UP_LEFT, False)],
                corners=1,
            ),
            CornerChecker(
                dir_in_region=[(DOWN, True), (RIGHT, True), (DOWN_RIGHT, False)],
                corners=1,
            ),
            CornerChecker(
                dir_in_region=[(DOWN, True), (LEFT, True), (DOWN_LEFT, False)],
                corners=1,
            ),
        )
        corners = 0
        all_region_pos = set()
        for k, v in region.items():
            if not v:
                all_region_pos.add(k)
                continue
            for pos in v:
                all_region_pos.add(pos)
        for pos in all_region_pos:
            for checker in corner_possibles:
                if all([
                    (self.tup_add(pos, dir) in all_region_pos) is cmp
                    for dir, cmp in checker.dir_in_region
                ]):
                    corners += checker.corners
        return corners

    def part_1(self):
        total = 0
        regions = []
        visited = set()
        for y in range(self._y_bound):
            for x in range(self._x_bound):
                if (x, y) in visited:
                    continue
                regions.append(self._setup_region(self.input_data[y][x], (x, y), visited))
        for region in regions:
            size = sum([1 for _ in region.keys()]) or 1
            perim = sum([4 - len(v) for v in region.values()]) or 4
            total += size * perim
        return total  # 1465968

    def part_2(self):
        total = 0
        regions = []
        visited = set()
        for y in range(self._y_bound):
            for x in range(self._x_bound):
                if (x, y) in visited:
                    continue
                regions.append(self._setup_region(self.input_data[y][x], (x, y), visited))
        for region in regions:
            size = sum([1 for _ in region.keys()]) or 1
            sides = self._count_corners(region)
            total += sides * size
        return total  # 897702


if __name__ == "__main__":
    d = Day12()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
