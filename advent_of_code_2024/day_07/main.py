from typing import Callable
from advent_of_code_2024.day import Day
from advent_of_code_2024.common import pad_left


def ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


class Day7(Day):
    def __init__(self):
        super().__init__(7, f"advent_of_code_2024/day_07/puzzle_input.txt")

    def _add(self, x: int, y: int) -> int:
        return x + y

    def _mult(self, x: int, y: int) -> int:
        return x * y

    def _concat(self, x: int, y: int) -> int:
        return int(str(x) + str(y))

    def _parse_line(self, line: str) ->tuple[int, list[int]]:
        first_t = line.split(": ")
        answer = int(first_t[0])
        args = list(map(int, first_t[1].split(" ")))
        return answer, args

    def _get_all_n_operator_combos(self, n: int) -> list[Callable]:
        if n < 1:
            raise ValueError("n must be at least 1")
        bin_combos = [bin(i) for i in range(2 ** (n))]
        combos = []
        for _bin in [pad_left(str(s).lstrip("0b"), n) for s in bin_combos]:
            callables = []
            for b in _bin:
                if b == "0":
                    callables.append(self._add)
                else:
                    callables.append(self._mult)
            combos.append(callables)
        return combos

    def _get_all_n_operator_combos_tern(self, n: int) -> list[Callable]:
        if n < 1:
            raise ValueError("n must be at least 1")
        bin_combos = [ternary(i) for i in range(3 ** (n))]
        combos = []
        for _bin in [pad_left(str(s), n) for s in bin_combos]:
            callables = []
            for b in _bin:
                if b == "0":
                    callables.append(self._add)
                elif b == "1":
                    callables.append(self._mult)
                else:
                    callables.append(self._concat)
            combos.append(callables)
        return combos

    def _evaluate_operations(self, operations: list[Callable], args: list[int]) -> int:
        left_arg = args[0]
        right_and_op = tuple(zip(args[1:], operations))
        for right_arg, op in right_and_op:
            left_arg = op(left_arg, right_arg)
        return left_arg

    def part_1(self):
        good_results = 0
        for line in self.input_data:
            answer, args = self._parse_line(line)
            combos = self._get_all_n_operator_combos(len(args) - 1)
            for combo in combos:
                test_answer = self._evaluate_operations(combo, args)
                # print(combo, args)
                if test_answer == answer:
                    good_results += answer
                    break
        return good_results  # 14711933466277

    def part_2(self):
        good_results = 0
        for line in self.input_data:
            answer, args = self._parse_line(line)
            combos = self._get_all_n_operator_combos_tern(len(args) - 1)
            for combo in combos:
                test_answer = self._evaluate_operations(combo, args)
                # print(combo, args)
                if test_answer == answer:
                    good_results += answer
                    break
        return good_results  # 14711933466277


if __name__ == "__main__":
    d = Day7()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
