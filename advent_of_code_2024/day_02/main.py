from operator import itemgetter
from advent_of_code_2024.day import Day


checkup_rule = lambda scan: any([
    all(1 <= x <= 3 for x in scan),
    all(-3 <= x <= -1 for x in scan),
])


class Day2(Day):
    def __init__(self):
        super().__init__(2, f"advent_of_code_2024/day_02/puzzle_input.txt")

    def _scan_report(self, report: list[int]) -> list[int]:
        scan = []
        for i in range(1, len(report)):
            scan.append(report[i] - report[i-1])
        return scan

    def _is_one_level_away(self, row: list[int]) -> bool:
        combinations = []
        for i in range(len(row)):
            combinations.append(itemgetter(*[x for x in range(len(row)) if x != i])(row))
        result = any(checkup_rule(self._scan_report(c)) for c in combinations)
        return result

    def part_1(self):
        safe_reports = 0
        for line in self.input_data:
            report = tuple(map(int, line.split(" ")))
            scan = self._scan_report(report)
            if checkup_rule(scan):
                safe_reports += 1
        return safe_reports  # 321

    def part_2(self):
        safe_reports = 0
        for line in self.input_data:
            report = tuple(map(int, line.split(" ")))
            scan = self._scan_report(report)
            if checkup_rule(scan):
                safe_reports += 1
            else:
                safe_reports += int(self._is_one_level_away(report))
        return safe_reports  # 389, too high; 373 too low; 386 just right
