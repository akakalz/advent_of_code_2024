from collections import defaultdict
from itertools import combinations
from advent_of_code_2024.day import Day


class Cartesian:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: "Cartesian") -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Point(Cartesian):
    def __add__(self, other: Cartesian) -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Cartesian) -> "Point":
        return Point(self.x - other.x, self.y - other.y)


class Direction(Cartesian):
    pass


class Day8(Day):
    def __init__(self):
        super().__init__(8, f"advent_of_code_2024/day_08/puzzle_input.txt")

        self._x_bound = len(self.input_data[0])
        self._y_bound = len(self.input_data)

    def _on_map(self, point: Point) -> bool:
        return all([
            0 <= point.x < self._x_bound,
            0 <= point.y < self._y_bound,
        ])

    def _add_tuples(self, t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    def _subtract_tuples(self, t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] - t2[0], t1[1] - t2[1]

    def _get_dir_between_two_points(self, p1: Point, p2: Point) -> Direction:
        return Direction(p1.x - p2.x, p1.y - p2.y)

    def _get_antenna_locations(self) -> dict[str, set[tuple[int, int]]]:
        antennas = defaultdict(set)
        for y, line in enumerate(self.input_data):
            for x, char in enumerate(line):
                if char == ".":
                    continue
                antennas[char].add((x, y))
        return antennas

    def _calc_antinodes(self, positions: set[tuple[int, int]]) -> set[tuple[int, int]]:
        antinodes = set()
        combos = tuple(combinations(positions, 2))
        for combo in combos:
            _dir = self._get_dir_between_two_points(Point(*combo[0]), Point(*combo[1]))
            p_combo_1 = Point(*combo[0])
            p_combo_2 = Point(*combo[1])
            p1 = p_combo_1 + _dir
            p2 = p_combo_1 - _dir
            p3 = p_combo_2 + _dir
            p4 = p_combo_2 - _dir
            if p1 != p_combo_1 and p1 != p_combo_2:
                antinodes.add(p1)
            if p2 != p_combo_1 and p2 != p_combo_2:
                antinodes.add(p2)
            if p3 != p_combo_1 and p3 != p_combo_2:
                antinodes.add(p3)
            if p4 != p_combo_1 and p4 != p_combo_2:
                antinodes.add(p4)
        return antinodes

    def _calc_multi_antinodes(self, positions: set[tuple[int, int]]) -> set[tuple[int, int]]:
        antinodes = set()
        combos = tuple(combinations(positions, 2))
        for combo in combos:
            base_1 = Point(*combo[0])
            base_2 = Point(*combo[1])
            _dir = self._get_dir_between_two_points(base_1, base_2)
            add_p1 = base_1 + _dir
            add_p2 = base_2 + _dir
            sub_p1 = base_1 - _dir
            sub_p2 = base_2 - _dir

            while self._on_map(add_p1):
                antinodes.add(add_p1)
                add_p1 = add_p1 + _dir
            while self._on_map(add_p2):
                antinodes.add(add_p2)
                add_p2 = add_p2 + _dir
            while self._on_map(sub_p1):
                antinodes.add(sub_p1)
                sub_p1 = sub_p1 - _dir
            while self._on_map(sub_p2):
                antinodes.add(sub_p2)
                sub_p2 = sub_p2 - _dir
        return antinodes

    def part_1(self):
        antinode_pos = set()
        antennas = self._get_antenna_locations()
        for positions in antennas.values():
            freq_antinodes = self._calc_antinodes(positions)
            antinode_pos = antinode_pos.union({x for x in freq_antinodes if self._on_map(x)})
        return len(antinode_pos)  # 320

    def part_2(self):
        antinode_pos = set()
        antennas = self._get_antenna_locations()
        for positions in antennas.values():
            freq_antinodes = self._calc_multi_antinodes(positions)
            antinode_pos = antinode_pos.union({x for x in freq_antinodes if self._on_map(x)})
        return len(antinode_pos)  # 1157


if __name__ == "__main__":
    d = Day8()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
