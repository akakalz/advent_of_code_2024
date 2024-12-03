import re
from advent_of_code_2024.day import Day


MUL_PATTERN = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")
BREAK_APART_MUL_PATTERN = re.compile(r"mul\((\d+),(\d+)\)")
MUL_WITH_DOS_PATTERN = re.compile(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")
DO = r"do()"
DONT = r"don't()"

class Day3(Day):
    def __init__(self):
        super().__init__(3, f"advent_of_code_2024/day_03/puzzle_input.txt")

    def part_1(self):
        answer = 0
        for line in self.input_data:
            match = MUL_PATTERN.findall(line)
            for m in match:
                x, y = tuple(map(int, BREAK_APART_MUL_PATTERN.match(m).groups()))
                answer += x * y
        return answer  # 170068701

    def part_2(self):
        answer = 0
        do = True
        for line in self.input_data:
            match = MUL_WITH_DOS_PATTERN.findall(line)
            for m in match:
                if m == DO:
                    do = True
                elif m == DONT:
                    do = False
                elif do:
                    x, y = tuple(map(int, BREAK_APART_MUL_PATTERN.match(m).groups()))
                    answer += x * y
        return answer  # 78683433
