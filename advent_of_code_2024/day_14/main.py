import re
from collections import defaultdict
from dataclasses import dataclass
from math import prod
from advent_of_code_2024.day import Day


POS_V_PATTERN = re.compile(r"^p=(.*?) v=(.*?)$")


@dataclass
class Robot:
    pos: tuple[int, int]
    vel: tuple[int, int]


class Day14(Day):
    def __init__(self):
        super().__init__(14, f"advent_of_code_2024/day_14/puzzle_input.txt")
        self.x_size = 101
        self.y_size = 103
        self.robots = self._arrange_data()

    def _arrange_data(self) -> list[Robot]:
        robots = []
        for line in self.input_data:
            match = POS_V_PATTERN.match(line)
            pos, vel = tuple(map(int, match.group(1).split(","))), tuple(map(int, match.group(2).split(",")))
            robots.append(Robot(pos, vel))
        return robots

    def _calc_bot_pos(self, bot: Robot, seconds: int) -> tuple[int, int]:
        non_tele_move = bot.vel[0] * seconds, bot.vel[1] * seconds
        new_bot_pos = (bot.pos[0] + non_tele_move[0]) % self.x_size, (bot.pos[1] + non_tele_move[1]) % self.y_size
        return new_bot_pos

    def _calc_quadrant(self, pos: tuple[int, int]) -> int:
        if 0 <= pos[0] < (self.x_size // 2) and 0 <= pos[1] < (self.y_size // 2):
            return 1
        if 0 <= pos[0] <= (self.x_size // 2) - 1 and self.y_size // 2 < pos[1] < self.y_size:
            return 2
        if self.x_size // 2 < pos[0] < self.x_size and 0 <= pos[1] < (self.y_size // 2):
            return 3
        if self.x_size // 2 < pos[0] < self.x_size and self.y_size // 2 < pos[1] < self.y_size:
            return 4
        return 0

    def _pretty_print_positions(self, all_bot_pos: dict, counter: int) -> None:
        rows = []
        cols = []
        for y in range(self.y_size):
            for x in range(self.x_size):
                cols.append("X" if (x, y) in all_bot_pos else " ")
            rows.append("".join(cols))
            cols = []
        pos_str = "\n".join(rows)
        with open(f"advent_of_code_2024/day_14/trees/xmas_tree_{counter}.txt", "w") as out_file:
            out_file.write(pos_str)
        # print("\n".join(rows))

    def part_1(self):
        total_seconds = 100
        all_pos = defaultdict(int)
        quads = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        for bot in self.robots:
            bot_pos = self._calc_bot_pos(bot, total_seconds)
            all_pos[bot_pos] += 1
            quads[self._calc_quadrant(bot_pos)] += 1
        return prod([v for k, v in quads.items() if k != 0])

    def part_2(self):
        counter = 1
        while counter < 10000:
            all_pos = defaultdict(int)
            for bot in self.robots:
                bot_pos = self._calc_bot_pos(bot, counter)
                all_pos[bot_pos] += 1
            if all([v == 1 for v in all_pos.values()]):
                # self._pretty_print_positions(all_pos, counter)
                break
            counter += 1
        return counter  # 7847

"""
                            X

                           X             X                                            X

                                                                             X
                                                                                            X
                X                               X
                             X
                                                        X                X  X
                 X            X                X                    X                   X       X
            X                                          X                           X X
         X                                X
                                                                          X           X         X
     X



 X         X
         X                                       X                          X                       X
                                                    X
                                                          X                      X
  X

                X                                                              X
          X                                                 X                  X
                                                  X
     X                           X
             X                                         X                                         X
                                                                           X
                                      X                                                            X
                                                                                      X
                                      X                          X              X        X   X
                                                                                    X
  X          X                              X

                                                                   X
                                                   X
                                                                              X
    X
         X


                                        X                                              X
                                                                                   X
                                                      X            X
              X                                                         X                         X
                                          X              X

               X                                 X
                                                                                                   X


       X                                                X
                                                                                   X
                                          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                                          X                             X                      X  X
                                          X                             X
                             X            X                             X
                                          X                             X
                                          X              X              X
                                          X             XXX             X
                                   X      X            XXXXX            X
        X                     X     XX    X           XXXXXXX           X
                                          X          XXXXXXXXX          X
                         X                X            XXXXX            X
                  X     X                 X           XXXXXXX           X
                                          X          XXXXXXXXX          X      X
                                          X         XXXXXXXXXXX         X                   XXX
                     X                    X        XXXXXXXXXXXXX        X
                     X     X              X          XXXXXXXXX          X
                                          X         XXXXXXXXXXX         X
                                          X        XXXXXXXXXXXXX        X    X
                                    X     X       XXXXXXXXXXXXXXX       X X        X     X
                                          X      XXXXXXXXXXXXXXXXX      X
                                          X        XXXXXXXXXXXXX        X                         X
                    X               X     X       XXXXXXXXXXXXXXX       X
                                          X      XXXXXXXXXXXXXXXXX      X  X
                                     X    X     XXXXXXXXXXXXXXXXXXX     X
                    X                  X  X    XXXXXXXXXXXXXXXXXXXXX    X
                       X                  X             XXX             X            X
                                          X             XXX             X
                                      X   X             XXX             X                  X
                                       X  X                             X           X
                                          X                             X
                                          X                             X     X            X
                                          X                             X
            X                             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       X

 X                                                             X

                               X                                 X

                                                             X
                          X
                                     X                  X           X
                                                  X                 X                      X
   X                                                                        X      X
                                                                      X   X
                    X
          X                                                                        X
X
                                          X                   X
                               X
"""


if __name__ == "__main__":
    d = Day14()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
