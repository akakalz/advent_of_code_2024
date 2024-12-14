from collections import deque
from typing import Union
from advent_of_code_2024.day import Day


class File:
    def __init__(self, id: int, size: int) -> None:
        self.id = id
        self.size = size

    def __str__(self) -> str:
        return f"{self.id}" * self.size

    def __hash__(self) -> int:
        return hash((self.id, self.size))

    def __int__(self) -> int:
        return self.id


class FreeSpace:
    def __init__(self, size: int) -> None:
        self.size = size

    def __str__(self) -> str:
        return "." * self.size


class Disk:
    def __init__(self, initial_state: str) -> None:
        self._state: list = self._render_state(initial_state)

    def __str__(self) -> str:
        return "".join([str(obj) for obj in self._state])

    def _render_state(self, initial_state: deque) -> list:
        array = []
        _id = 0
        for i in range(0, len(initial_state), 2):
            j = i + 1
            block = int(initial_state[i])
            file = File(_id, block)
            array.append(file)
            try:
                free = FreeSpace(int(initial_state[j]))
                array.append(free)
            except IndexError:
                pass
            _id += 1
        return array

    def _get_free_space_positions(self) -> list[tuple[int, list[FreeSpace]]]:
        free_spaces = []
        for i, item in enumerate(self._state):
            if isinstance(item, FreeSpace):
                free_spaces.append((i, item))
        return free_spaces

    def _move_file(self, file: File, from_idx: int, to_idx: int) -> None:
        del self._state[from_idx]
        if isinstance(self._state[from_idx - 1], FreeSpace):
            self._state[from_idx - 1].size += file.size
        elif isinstance(self._state[from_idx], FreeSpace):
            self._state[from_idx].size += file.size
        else:
            self._state.insert(from_idx, FreeSpace(file.size))
        self._state.insert(to_idx, file)

    def defrag(self) -> None:
        """
        rearranges the state to fill as many open spaces toward the beginning of the disk
        """
        no_space_or_moved = set()
        defragged = False
        while not defragged:
            free_spaces = self._get_free_space_positions()
            for idx in range(len(self._state) - 1, 0, -1):
                if isinstance(self._state[idx], File) and self._state[idx] not in no_space_or_moved:
                    item_to_move: File = self._state[idx]
                    for _, free_space in enumerate(free_spaces):
                        if item_to_move.size <= free_space[1].size and idx > free_space[0]:
                            free_space[1].size -= item_to_move.size
                            self._move_file(item_to_move, idx, free_space[0])
                            no_space_or_moved.add(item_to_move)
                            break
                    else:
                        no_space_or_moved.add(item_to_move)
                    break
            else:
                defragged = True

    def get_state(self) -> list[Union[File,FreeSpace]]:
        return self._state

    def checksum(self) -> int:
        counter = 0
        checksum = 0
        for item in self._state:
            if isinstance(item, FreeSpace):
                counter += item.size
            else:
                for _ in range(item.size):
                    checksum += counter * item.id
                    counter += 1
        return checksum

class Day9(Day):
    def __init__(self):
        super().__init__(9, f"advent_of_code_2024/day_09/puzzle_input.txt")
        self.input_data = self.input_data[0]  # single line

    def _checksum(self, array: list) -> int:
        checksum = 0
        for i, num in enumerate(array):
            if num is None or num == "." or isinstance(num, FreeSpace):
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

    def part_1(self):
        array = self._render_inital_array()
        array = self._sort_array(array)
        return self._checksum(array)  # 6384282079460

    def part_2(self):
        disk = Disk(self.input_data)
        disk.defrag()
        return disk.checksum()  # 6408966547049


if __name__ == "__main__":
    d = Day9()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
