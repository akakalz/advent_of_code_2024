from advent_of_code_2024.day import Day


class Day5(Day):
    def __init__(self):
        super().__init__(5, f"advent_of_code_2024/day_05/puzzle_input.txt")

    def _restructure_input(self) -> tuple[dict, list]:
        switch = False
        rules = {}
        updates = []
        for line in self.input_data:
            if not line:
                switch = True
                continue
            if not switch:
                x, y = tuple(map(int, line.split("|")))
                if x not in rules:
                    rules[x] = set()
                rules[x].add(y)
            else:
                updates.append(list(map(int, line.split(","))))
        return rules, updates

    def _is_correct_order(self, rules: dict, update: list[int]) -> bool:
        checks = {}
        for i, num in enumerate(update):
            checks[num] = i
        for num in update:
            if not all([
                checks[num] < checks[compare_num] or compare_num not in rules.get(num, set())
                for compare_num in [x for x in checks.keys() if x != num]
            ]):
                return False
        return True

    def _correct_orderings(self, rules: dict, update: list[int]) -> list[int]:
        update_set = set(update)
        order_dict = {
            num: {k for k in update_set if k != num and k in rules.get(num, set())}
            for num in update
        }
        return sorted(update, key=lambda x: len(order_dict.get(x, set())), reverse=True)

    def part_1(self):
        answer = 0
        rules, updates = self._restructure_input()
        for update in updates:
            if self._is_correct_order(rules, update):
                answer += update[len(update) // 2]
        return answer  # 5087

    def part_2(self):
        answer = 0
        rules, updates = self._restructure_input()
        for update in updates:
            if not self._is_correct_order(rules, update):
                corrected = self._correct_orderings(rules, update)
                answer += corrected[len(corrected) // 2]
        return answer  # 4971
