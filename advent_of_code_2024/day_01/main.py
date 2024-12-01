from collections import defaultdict
from advent_of_code_2024.day import Day


class Day1(Day):
    def __init__(self):
        super().__init__(1, f"advent_of_code_2024/day_01/puzzle_input.txt")

    def part_1(self):
        answer = 0
        left = []
        right = []
        for line in self.input_data:
            numbers = line.split("   ")
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
        left.sort()
        right.sort()
        for i in range(len(left)):
            answer += abs(left[i] - right[i])
        return answer  # 3714264

    def part_2(self):
        answer = 0
        left = []
        right = defaultdict(int)
        for line in self.input_data:
            numbers = line.split("   ")
            left.append(int(numbers[0]))
            right[int(numbers[1])] += 1
        for num in left:
            answer += num * right[num]
        return answer  # 18805872
