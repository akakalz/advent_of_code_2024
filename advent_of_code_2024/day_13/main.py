import re
from dataclasses import dataclass
# from sympy import Symbol
from advent_of_code_2024.day import Day


X_Y_PATTERN = re.compile(r"^.+[+=](\d*), .*[+=](\d*)$")
A_COST = 3
B_COST = 1


@dataclass
class Arcade:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


class Day13(Day):
    def __init__(self):
        super().__init__(13, f"advent_of_code_2024/day_13/puzzle_input.txt")
        self.arcades = self._arrange_input()

    def _arrange_input(self) -> list[Arcade]:
        def yield_lines():
            for line in self.input_data:
                yield line

        arcades = []
        lines = yield_lines()
        next_line = next(lines, None)
        a = None
        b = None
        p = None
        while next_line is not None:
            while next_line:
                match = X_Y_PATTERN.match(next_line)
                a = int(match.group(1)), int(match.group(2))
                next_line = next(lines, None)

                match = X_Y_PATTERN.match(next_line)
                b = int(match.group(1)), int(match.group(2))
                next_line = next(lines, None)

                match = X_Y_PATTERN.match(next_line)
                p = int(match.group(1)), int(match.group(2))
                next_line = next(lines, None)

                arcades.append(Arcade(a, b, p))
                next_line = next(lines, None)

        return arcades

    def part_1(self):
        winnables = []
        max_press = 100
        for arcade in self.arcades:
            for i in range(max_press, 0, -1):
                if all([
                    (arcade.prize[0] - (arcade.button_b[0] * i)) % arcade.button_a[0] == 0,
                    (arcade.prize[1] - (arcade.button_b[1] * i)) % arcade.button_a[1] == 0,
                    (arcade.prize[0] - (arcade.button_b[0] * i)) // arcade.button_a[0] == \
                        (arcade.prize[1] - (arcade.button_b[1] * i)) // arcade.button_a[1]
                ]):
                    winnables.append((arcade, i, (arcade.prize[1] - (arcade.button_b[1] * i)) // arcade.button_a[1]))
                    break
        print(len(winnables))
        return sum([w[1] + (w[2] * 3) for w in winnables])  # 29711

    def part_2(self):
        winnables = []
        off_set = 10_000_000_000_000
        max_press = 10000
        for arcade in self.arcades:
            arcade.prize[0], arcade.prize[1] = arcade.prize[0] + off_set, arcade.prize[1] + off_set
            for i in range(max_press, 0, -1):
                if all([
                    (arcade.prize[0] - (arcade.button_b[0] * i)) % arcade.button_a[0] == 0,
                    (arcade.prize[1] - (arcade.button_b[1] * i)) % arcade.button_a[1] == 0,
                    (arcade.prize[0] - (arcade.button_b[0] * i)) // arcade.button_a[0] == \
                        (arcade.prize[1] - (arcade.button_b[1] * i)) // arcade.button_a[1]
                ]):
                    winnables.append((arcade, i, (arcade.prize[1] - (arcade.button_b[1] * i)) // arcade.button_a[1]))
                    break
        print(len(winnables))
        return sum([w[1] + (w[2] * 3) for w in winnables])  # 29711


if __name__ == "__main__":
    d = Day13()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
