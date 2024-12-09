from collections import deque, defaultdict
from advent_of_code_2024.day import Day


class Day9(Day):
    def __init__(self):
        super().__init__(9, f"advent_of_code_2024/day_09/puzzle_input.txt")
        self.input_data = self.input_data[0]  # single line

    def _checksum(self, array: list) -> int:
        checksum = 0
        for i, num in enumerate(array):
            if num is None:
                continue
            checksum += i * int(num)
        return checksum

    def _render_inital_array(self) -> deque:
        array = deque()
        _id = 0
        for i in range(0, len(self.input_data), 2):
            j = i + 1
            block = int(self.input_data[i])
            array.extend([_id] * block)
            try:
                free = int(self.input_data[j])
                array.extend([None] * free)
            except IndexError:
                pass
            _id += 1
        return array

    def _sort_array(self, array: deque) -> list:
        sorted_array = []
        while array:
            left = array.popleft()
            if left is not None:
                sorted_array.append(left)
            else:
                try:
                    right = array.pop()
                    while right is None:
                        right = array.pop()
                    sorted_array.append(right)
                except IndexError:
                    pass
        return sorted_array

    def _scan_contiguous_free_space(self, array: deque) -> dict[int, list[int]]:
        free_spaces = defaultdict(list)
        is_free = False
        last_idx = -1
        for i, item in enumerate(array):
            if item is None:
                if not is_free:
                    last_idx = i
                else:
                    free_spaces[last_idx].append(i)
                is_free = True
            else:
                is_free = False
        return free_spaces

    def _sort_to_fill_size(self, array: deque) -> list:
        previous_moved_items = -1
        moved_items = 0
        # while moved_items != previous_moved_items:
        #     pass
        return []

    def part_1(self):
        array = self._render_inital_array()
        array = self._sort_array(array)
        return self._checksum(array)  # 6384282079460

    def part_2(self):
        array = self._render_inital_array()
        array = self._sort_to_fill_size(array)
        return self._checksum(array)  # ???


if __name__ == "__main__":
    d = Day9()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
