from collections import Counter
from functools import lru_cache
from print_aoc import print_task1, print_task2
from file_util import read_line_seperated_data_sets


@lru_cache(maxsize=None)
def count(adjacent_elements: str, steps: int) -> Counter:
    return Counter(adjacent_elements) if steps == 0 else \
        sum((count(adjacent_elements[i:i + 2], steps) for i in range(len(adjacent_elements) - 1)), Counter()) - Counter(adjacent_elements[1:-1]) if len(adjacent_elements) > 2 else \
        count(adjacent_elements[0] + rules[adjacent_elements], steps - 1) + count(rules[adjacent_elements] + adjacent_elements[1], steps - 1) - Counter(rules[adjacent_elements])


def solve(steps: int, polymer_template: str) -> int:
    counted = count(polymer_template, steps)
    most_common = counted.most_common()
    return most_common[0][1] - most_common[-1][1]


if __name__ == "__main__":
    lines = read_line_seperated_data_sets()
    rules = lines[1].rstrip().split('\n')
    rules = dict(rule.split(" -> ") for rule in rules)
    print_task1(14, solve(10, lines[0]))
    print_task2(14, solve(40, lines[0]))
