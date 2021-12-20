from builtins import int
from typing import Any
from print_aoc import print_task1, print_task2
from file_util import read_lines
from functools import reduce
import itertools
import math
import json


def explode_if_four_pairs(x, pair_counter=4) -> tuple[bool, None, Any, None]:
    if isinstance(x, int):
        return False, None, x, None
    if pair_counter == 0:
        return True, x[0], 0, x[1]
    a, b = x
    did_explode, left, a, right = explode_if_four_pairs(a, pair_counter - 1)
    if did_explode:
        return True, left, [a, add_to_left(b, right)], None
    did_explode, left, b, right = explode_if_four_pairs(b, pair_counter - 1)
    if did_explode:
        return True, None, [add_to_right(a, left), b], right
    return False, None, x, None


def add_to_left(x, n) -> int | list:
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [add_to_left(x[0], n), x[1]]


def add_to_right(x, n) -> int | list:
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [x[0], add_to_right(x[1], n)]


def split_if_greater_ten(x: list | int):
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, math.ceil(x / 2)]
        return False, x
    a, b = x
    did_split, a = split_if_greater_ten(a)
    if did_split:
        return True, [a, b]
    did_split, b = split_if_greater_ten(b)
    return did_split, [a, b]


def add(a: list, b: list) -> list:
    x = [a, b]
    while True:
        did_explode, _, x, _ = explode_if_four_pairs(x)
        if did_explode:
            continue
        did_split, x = split_if_greater_ten(x)
        if not did_split:
            break
    return x


def calc_magnitude_of_sum(x: list) -> int:
    return x if isinstance(x, int) else 3 * calc_magnitude_of_sum(x[0]) + 2 * calc_magnitude_of_sum(x[1])


if __name__ == "__main__":
    lines = list(map(json.loads, read_lines()))
    print_task1(18, calc_magnitude_of_sum(reduce(add, lines)))
    print_task2(18, max(calc_magnitude_of_sum(add(a, b)) for a, b in itertools.permutations(lines, 2)))
