from advent_of_code_2024.day import Day


class Direction:
    up = (0, -1)
    down = (0, 1)
    left = (-1, 0)
    right = (1, 0)

class Day6(Day):
    def __init__(self):
        super().__init__(6, f"advent_of_code_2024/day_06/puzzle_input.txt")

        self._start_pos = self._get_initial_pos()

    def _get_initial_pos(self) -> tuple[int, int]:
        for y in range(len(self.input_data)):
            for x in range(len(self.input_data[0])):
                if self.input_data[y][x] == "^":
                    return (x, y)
        else:
            raise ValueError("start pos not found")

    def _turn_right(self, current_dir: tuple[int, int]) -> tuple[int, int]:
        if current_dir == Direction.up:
            return Direction.right
        if current_dir == Direction.right:
            return Direction.down
        if current_dir == Direction.down:
            return Direction.left
        if current_dir == Direction.left:
            return Direction.up

    def _on_map(self, pos: tuple[int, int]) -> bool:
        return all([
            0 <= pos[0] < len(self.input_data[0]),
            0 <= pos[1] < len(self.input_data),
        ])

    def _move(self, current_dir: tuple[int, int], current_pos: tuple[int, int]) -> tuple:
        adjustment = self._add_tuple(current_pos, current_dir)
        if not self._on_map(adjustment):
            pass
        elif self.input_data[adjustment[1]][adjustment[0]] == "#":
            current_dir = self._turn_right(current_dir)
            adjustment = self._add_tuple(current_pos, current_dir)
        return current_dir, adjustment

    def _check_perimeter(self, vertices: tuple[tuple[int, int]]) -> bool:
        combos = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
        ]
        return all([
            self._check_path(vertices[c[0]], vertices[c[1]])
            for c in combos
        ])

    def _add_tuple(self, t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    def _check_path(self, start: tuple[int, int], end: tuple[int, int]) -> bool:
        return all([
            self.input_data[p[1]][p[0]] != "#" and p != self._start_pos
            for p in self._get_points_between_two_points(start, end)
        ])

    def _get_points_between_two_points(self, p1: tuple[int, int], p2: tuple[int, int]) -> tuple[tuple[int, int]]:
        if p1 == p2:
            raise ValueError("no points between the same point")
        # (4,6), (4, 1) -> [(4,6), (4,5), (4,4), (4,3), (4,2), (4,1)]
        dist = p1[0] - p2[0], p1[1] - p2[1]
        if not dist[0]:
            x = False
            dir = dist[0], dist[1] // abs(dist[1])
            num = abs(dist[1])
            negative = dist[1] < 0
        else:
            x = True
            dir = dist[0] // abs(dist[0]), dist[1]
            num = abs(dist[0])
            negative = dist[0] < 0

        if x:
            pass

        iters = list()
        return

    def part_1(self):
        visited_pos = set()
        current_dir = Direction.up
        current_pos = self._start_pos
        while self._on_map(current_pos):
            visited_pos.add(current_pos)
            current_dir, current_pos = self._move(current_dir, current_pos)
        return len(visited_pos)  # 4665

    def part_2(self):
        """
        some point after crossing path after the 3rd turn? no.. not quite
        definitely something where you build a rectangle though
        """
        actions_taken = []
        visited_pos = []
        current_dir = Direction.up
        current_pos = self._start_pos
        while self._on_map(current_pos):
            visited_pos.append(current_pos)
            old_dir = current_dir
            current_dir, current_pos = self._move(current_dir, current_pos)
            if current_dir == old_dir:
                actions_taken.append("straight")
            else:
                actions_taken.append(("turn", "straight"))
        print(visited_pos)
        print(actions_taken)
        return len(visited_pos)  # 4665
