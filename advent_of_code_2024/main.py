from advent_of_code_2024 import *  # all days and the day base class


days = {
    "1": Day1,
    "2": Day2,
    "3": Day3,
    "4": Day4,
    "5": Day5,
    "6": Day6,
    "7": Day7,
    "8": Day8,
    "9": Day9,
    "10": Day10,
    "11": Day11,
    "12": Day12,
    "13": Day13,
    "14": Day14,
    "15": Day15,
    "16": Day16,
    "17": Day17,
    "18": Day18,
    "19": Day19,
    "20": Day20,
    "21": Day21,
    "22": Day22,
    "23": Day23,
    "24": Day24,
    "25": Day25,
}


if __name__ == "__main__":
    print("Enter day to run: (e.g. 8)")
    day = input()

    if day not in days:
        raise ValueError(f"value not recognized: {day}\n\tPlease enter a number 1 to 25")

    d: Day = days[day]()
    print(f"== {str(d)} ====================")
    print(f"    part 1: {d.part_1()}")
    print(f"    part 2: {d.part_2()}")
    print("FIN")
