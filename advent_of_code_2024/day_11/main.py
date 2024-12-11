from collections import defaultdict
from advent_of_code_2024.day import Day


class Day11(Day):
    def __init__(self):
        super().__init__(11, f"advent_of_code_2024/day_11/puzzle_input.txt")

    """
    rules
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    """

    def _split_stone(self, stone: int) -> tuple[int, int]:
        str_stone = str(stone)
        return int(str_stone[0:(len(str_stone) // 2)]), int(str_stone[(len(str_stone) // 2):])

    def _calc_values(self, stone: int) -> list[int]:
        new_stones = []
        if stone == 0:
            new_stones.append(1)
        elif not len(str(stone)) % 2:
            new_stones.extend(self._split_stone(stone))
        else:
            new_stones.append(2024 * stone)
        return new_stones

    def part_1(self):
        blinks = 25
        self.stones = list(map(int, self.input_data[0].split(" ")))
        for _ in range(blinks):
            new_stones = []
            for stone in self.stones:
                if stone == 0:
                    new_stones.append(1)
                elif not len(str(stone)) % 2:
                    new_stones.extend(self._split_stone(stone))
                else:
                    new_stones.append(2024 * stone)
            self.stones = new_stones
        return len(self.stones)  # 198075

    def part_2(self):
        self.stones = list(map(int, self.input_data[0].split(" ")))
        basic_cache = {}
        stone_storage = defaultdict(int)
        for num in self.stones:
            stone_storage[num] += 1
        blinks = 75
        for _ in range(blinks):
            new_stone_storage = defaultdict(int)
            for k, v in stone_storage.items():
                if k not in basic_cache:
                    basic_cache[k] = self._calc_values(k)
                for stone in basic_cache[k]:
                    new_stone_storage[stone] += v
            stone_storage = new_stone_storage
        return sum(stone_storage.values())  # 235571309320764


if __name__ == "__main__":
    d = Day11()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
