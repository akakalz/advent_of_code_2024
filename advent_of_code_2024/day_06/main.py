import copy
from advent_of_code_2024.day import Day


class Direction:
    up = (0, -1)
    down = (0, 1)
    left = (-1, 0)
    right = (1, 0)


def replace_char_at_index(string, index, new_char):
    """Replaces the character at a specific index in a string with a new character."""

    # Convert the string to a list of characters
    char_list = list(string)

    # Replace the character at the specified index
    char_list[index] = new_char

    # Join the list of characters back into a string
    return "".join(char_list)


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

    def _on_map(self, pos: tuple[int, int], map: list[list[str]] = None) -> bool:
        if not map:
            map = self.input_data
        return all([
            0 <= pos[0] < len(map[0]),
            0 <= pos[1] < len(map),
        ])

    def _move(self, dir: tuple[int, int], pos: tuple[int, int], map=None) -> tuple[tuple[int, int], tuple[int, int]]:
        if not map:
            map = self.input_data
        new_pos = self._add_tuple(pos, dir)
        if self._on_map(new_pos, map=map) and map[new_pos[1]][new_pos[0]] == "#":
            dir = self._turn_right(dir)
            new_pos = pos
        return dir, new_pos

    def _add_tuple(self, t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    def _is_loop(self, _map: list[list[str]], dir: tuple[int, int], pos: tuple[int, int]) -> bool:
        # print("is loop check")
        # for line in _map:
        #     print(line)
        visited_pos = set()
        while self._on_map(pos, map=_map):
            visited_pos.add((dir, pos))
            dir, pos = self._move(dir, pos, map=_map)
            if (dir, pos) in visited_pos:
                # print("yay")
                return True
        # print("boo")
        return False

    def part_1(self):
        visited_pos = set()
        current_dir = Direction.up
        current_pos = self._start_pos
        while self._on_map(current_pos):
            visited_pos.add(current_pos)
            current_dir, current_pos = self._move(current_dir, current_pos)
        return len(visited_pos)  # 4665

    def part_2(self):
        obstructions_placed = []
        current_dir = Direction.up
        current_pos = self._start_pos
        while self._on_map(current_pos):
            # always try to block the guard's path on each move
            obstruction = self._add_tuple(current_pos, current_dir)
            if not self._on_map(obstruction) or self.input_data[obstruction[1]][obstruction[0]] == "#":
                pass
            else:
                map = copy.deepcopy(self.input_data)
                # print(f"old map line {obstruction[1]} = {map[obstruction[1]]}")
                map[obstruction[1]] = replace_char_at_index(map[obstruction[1]], obstruction[0], "#")
                # print(f"new map line {obstruction[1]} = {map[obstruction[1]]}")
                if self._is_loop(map, current_dir, current_pos):
                    obstructions_placed.append(obstruction)
            current_dir, current_pos = self._move(current_dir, current_pos)
            # print("new pos or dir")
        # print(obstructions_placed)
        return len(set(obstructions_placed))  # 252: too low, 1588 too low... 1740 right for diff set


if __name__ == "__main__":
    d = Day6()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
