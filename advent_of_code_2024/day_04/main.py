from advent_of_code_2024.day import Day


class Day4(Day):
    directions = {
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
        (1, 0),
        (-1, 0),
    }

    word_search = {
        0: "X",
        1: "M",
        2: "A",
        3: "S",
    }

    x_dirs = {
        (
            ((-1, -1), "M"),
            ((1, 1), "S"),
            ((-1, 1), "M"),
            ((1, -1), "S"),
        ),
        (
            ((-1, 1), "M"),
            ((1, -1), "S"),
            ((1, 1), "M"),
            ((-1, -1), "S"),
        ),
        (
            ((1, 1), "M"),
            ((-1, -1), "S"),
            ((1, -1), "M"),
            ((-1, 1), "S"),
        ),
        (
            ((1, -1), "M"),
            ((-1, 1), "S"),
            ((-1, -1), "M"),
            ((1, 1), "S"),
        ),
    }

    min_x = 0
    min_y = 0

    def __init__(self):
        super().__init__(4, f"advent_of_code_2024/day_04/puzzle_input.txt")

    def _check_dir(self, x: int, y: int, direction: tuple[int, int]) -> bool:
        result = False
        for i in range(1, 4):
            x += direction[0]
            y += direction[1]
            if any([
                x < self.min_x,
                y < self.min_y,
                x >= len(self.input_data),
                y >= len(self.input_data),
            ]):
                break
            if self.input_data[y][x] != self.word_search[i]:
                break
        else:
            result = True

        return result

    def _check_x(self, x: int, y: int, x_dir: tuple[tuple[int, int], str]) -> bool:
        a_pos = (x, y)
        result = False

        for tup, letter in x_dir:
            x1 = a_pos[0] + tup[0]
            y1 = a_pos[1] + tup[1]
            if any([
                x1 < self.min_x,
                y1 < self.min_y,
                x1 >= len(self.input_data),
                y1 >= len(self.input_data),
            ]):
                break
            if not self.input_data[y1][x1] == letter:
                break
        else:
            result = True

        return result

    def part_1(self):
        answer = 0
        for y in range(len(self.input_data)):
            for x in range(len(self.input_data)):
                if self.input_data[y][x] == "X":
                    for dir in self.directions:
                        answer += int(self._check_dir(x, y, dir))
        return answer  # 2642

    def part_2(self):
        answer = 0
        for y in range(len(self.input_data)):
            for x in range(len(self.input_data)):
                if self.input_data[y][x] == "A":
                    for dir in self.x_dirs:
                        answer += int(self._check_x(x, y, dir))
        return answer  # 1974
