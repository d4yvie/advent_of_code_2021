from print_aoc import print_task1, print_task2
from file_util import read_first_line
from collections import defaultdict
import itertools
import re


def parse_ints(line) -> list[int]:
    return list(map(int, re.findall(r"-?[0-9]+", line)))


def task1(y_start: int) -> int:
    yd_max = -y_start - 1
    return yd_max * (yd_max + 1) // 2


def task2(x_start: int, x_end: int, y_start: int, y_end: int) -> int:
    return simulate_steps(create_y_lists(y_start, y_end), create_x_sets(x_start, x_end))


def simulate_steps(y_lists: dict[int: list[int]], x_sets: dict[int: set[int] | int]) -> int:
    count = 0
    for y_list in y_lists.values():
        for x_set in x_sets.values():
            if isinstance(x_set, int):
                if any(i >= x_set for i in y_list):
                    count += 1
            elif any(i in x_set for i in y_list):
                count += 1
    return count


def create_y_lists(y_start: int, y_end: int) -> dict[int: list[int]]:
    initial_y_values = defaultdict(list)
    for init in range(y_start, -y_start):
        y, yd = 0, init
        for i in itertools.count(1):
            y += yd
            yd -= 1
            if y_start <= y <= y_end:
                initial_y_values[init].append(i)
            elif y < y_start:
                break
    return initial_y_values


def create_x_sets(x_start: int, x_end: int) -> dict[int: set[int] | int]:
    initial_x_values = defaultdict(set)
    for init in range(1, x_end + 1):
        x, xd = 0, init
        for i in itertools.count(1):
            x += xd
            if xd > 0:
                xd -= 1
            if xd == 0:
                if x_start <= x <= x_end:
                    initial_x_values[init] = min(initial_x_values[init], default=i)
                break
            if x_start <= x <= x_end:
                initial_x_values[init].add(i)
            elif x > x_end:
                break
    return initial_x_values


if __name__ == "__main__":
    x_start, x_end, y_start, y_end = parse_ints(read_first_line())
    print_task1(17, task1(y_start))
    print_task2(17, task2(x_start, x_end, y_start, y_end))
