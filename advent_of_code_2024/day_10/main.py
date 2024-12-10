from collections import defaultdict
from advent_of_code_2024.day import Day


class Day10(Day):
    def __init__(self):
        super().__init__(10, f"advent_of_code_2024/day_10/puzzle_input.txt")
        self._x_bound = len(self.input_data[0])
        self._y_bound = len(self.input_data)
        self._dirs = {(0, 1), (1, 0), (-1, 0), (0, -1)}

    def _on_map(self, pos) -> bool:
        return all([
            0 <= pos[0] < self._x_bound,
            0 <= pos[1] < self._y_bound,
        ])

    def _get_trailheads(self) -> list[tuple[int, int]]:
        my_list = []
        for y in range(self._y_bound):
            for x in range(self._x_bound):
                if self.input_data[y][x] == "0":
                    my_list.append((x, y))
        return my_list

    def _follow_trails(self, start_pos: tuple[int, int]) -> set:
        visited_pos = set()
        success_pos = set()
        self._follow_trails_helper(visited_pos, start_pos, success_pos)
        return success_pos

    def _follow_trails_helper(self, visited_pos: set, cur_pos: tuple[int, int], success_pos: set) -> None:
        pos_value = self.input_data[cur_pos[1]][cur_pos[0]]
        visited_pos.add(cur_pos)
        if pos_value == "9":
            success_pos.add(cur_pos)
            return
        path_forward = False
        for dir in self._dirs:
            new_pos = cur_pos[0] + dir[0], cur_pos[1] + dir[1]
            if self._on_map(new_pos) and \
            int(pos_value) + 1 == int(self.input_data[new_pos[1]][new_pos[0]]) and \
            new_pos not in visited_pos:
                path_forward = True
                self._follow_trails_helper(visited_pos, new_pos, success_pos)
        if not path_forward:
            return

    def _rate_trails(self, start_pos: tuple[int, int]) -> int:
        success_pos = defaultdict(int)
        self._rate_trails_helper(start_pos, success_pos)
        return sum(success_pos.values())

    def _rate_trails_helper(self, cur_pos: tuple[int, int], success_pos: dict) -> None:
        pos_value = self.input_data[cur_pos[1]][cur_pos[0]]
        if pos_value == "9":
            success_pos[cur_pos] += 1
            return
        path_forward = False
        for dir in self._dirs:
            new_pos = cur_pos[0] + dir[0], cur_pos[1] + dir[1]
            if self._on_map(new_pos) and int(pos_value) + 1 == int(self.input_data[new_pos[1]][new_pos[0]]):
                path_forward = True
                self._rate_trails_helper(new_pos, success_pos)
        if not path_forward:
            return

    def part_1(self):
        total = 0
        trailheads = self._get_trailheads()
        for trailhead in trailheads:
            total += len(self._follow_trails(trailhead))
        return total  # 501

    def part_2(self):
        total = 0
        trailheads = self._get_trailheads()
        for trailhead in trailheads:
            total += self._rate_trails(trailhead)
        return total  # 1017


if __name__ == "__main__":
    d = Day10()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
