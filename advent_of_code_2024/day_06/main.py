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

    def _move(self, current_dir: tuple[int, int], current_pos: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
        new_pos = self._add_tuple(current_pos, current_dir)
        if not self._on_map(new_pos):
            pass
        elif self.input_data[new_pos[1]][new_pos[0]] == "#":
            current_dir = self._turn_right(current_dir)
            new_pos = self._add_tuple(current_pos, current_dir)
        return current_dir, new_pos

    def _add_tuple(self, t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    def part_1(self):
        visited_pos = set()
        current_dir = Direction.up
        current_pos = self._start_pos
        while self._on_map(current_pos):
            visited_pos.add(current_pos)
            current_dir, current_pos = self._move(current_dir, current_pos)
        return len(visited_pos)  # 4665

    def part_2(self):
        visited_pos = set()
        obstructions_placed = 0
        current_dir = Direction.up
        current_pos = self._start_pos
        while self._on_map(current_pos):
            visited_pos.add(current_pos)
            current_dir, current_pos = self._move(current_dir, current_pos)
            # look around if you can get back on the path with a turn to the right
            test_dir = self._turn_right(current_dir)
            test_pos = self._add_tuple(test_dir, current_pos)
            if test_pos in visited_pos:
                obstructions_placed += 1
            # if current_pos == self._start_pos:
            #     print(test_dir)
            #     print(test_pos)
            #     print(visited_pos)
        return obstructions_placed  # ???
