from collections import defaultdict
from advent_of_code_2024.day import Day


# class Node:
#     __slots__ = ("up", "right", "down", "left", "coords")
#     up: "Node" = None
#     right: "Node" = None
#     down: "Node" = None
#     left: "Node" = None

#     coords: tuple[int, int]

#     def __hash__(self) -> int:
#         return hash(self.coords)


# class Region:
#     __slots__ = ("root", "size")
#     root: Node
#     size: int
#     all_nodes: set

#     def __init__(self, root: Node) -> None:
#         self.root = root

#         self._measure_region()

#     def _measure_region(self) -> None:
#         visited = set()
#         self._measure_helper(visited, self.root)
#         self.all_nodes = visited
#         self.size = len(visited)

#     def _measure_helper(self, visited: set[Node], cur_node: Node) -> None:
#         visited.add(cur_node)
#         if cur_node.up is not None and cur_node.up not in visited:
#             self._measure_helper(visited, cur_node.up)
#         if cur_node.right is not None and cur_node.right not in visited:
#             self._measure_helper(visited, cur_node.right)
#         if cur_node.down is not None and cur_node.down not in visited:
#             self._measure_helper(visited, cur_node.down)
#         if cur_node.left is not None and cur_node.left not in visited:
#             self._measure_helper(visited, cur_node.left)


class Day12(Day):
    def __init__(self):
        super().__init__(12, f"advent_of_code_2024/day_12/puzzle_input.txt")
        self._x_bound = len(self.input_data[0])
        self._y_bound = len(self.input_data)
        self.directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

    def _on_map(self, pos: tuple[int, int]) -> bool:
        return all([
            0 <= pos[0] < self._x_bound,
            0 <= pos[1] < self._y_bound,
        ])

    def tup_add(self, t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    def _setup_region(self, label: str, start_pos: tuple[int, int], total_visited: set) -> dict:
        region = defaultdict(int)
        self._setup_helper(label, start_pos, region, total_visited)
        return region

    def _setup_helper(self, label: str, cur_pos: tuple[int, int], region: defaultdict, total_visited: set) -> None:
        total_visited.add(cur_pos)
        for d in self.directions:
            nc, nr = self.tup_add(cur_pos, d)
            if not self._on_map((nc, nr)):
                continue
            if self.input_data[nr][nc] == label:
                region[cur_pos] += 1
                if (nc, nr) not in total_visited:
                    self._setup_helper(label, (nc, nr), region, total_visited)

    def part_1(self):
        total = 0
        regions = []
        visited = set()
        for y in range(self._y_bound):
            for x in range(self._x_bound):
                if (x, y) in visited:
                    continue
                regions.append(self._setup_region(self.input_data[y][x], (x, y), visited))
        for region in regions:
            size = sum([1 for _ in region.keys()]) or 1
            perim = sum([4 - v for v in region.values()]) or 4
            print(size, perim)
            total += size * perim
        return total  # 1465968

    def part_2(self):
        total = 0
        regions = []
        visited = set()
        for y in range(self._y_bound):
            for x in range(self._x_bound):
                if (x, y) in visited:
                    continue
                regions.append(self._setup_region(self.input_data[y][x], (x, y), visited))
        return total


if __name__ == "__main__":
    d = Day12()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
