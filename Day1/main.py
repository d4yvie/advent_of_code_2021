from file_util import read_lines
from print_aoc import finish_task1, finish_task2


def larger_sums(parsed_lines: list[str], window=1) -> int:
    return sum(b > a for a, b in zip(parsed_lines, parsed_lines[window:]))


if __name__ == '__main__':
    parsed_line = [int(line) for line in read_lines()]
    finish_task1(1, larger_sums(parsed_line), 1559)
    finish_task2(1, larger_sums(parsed_line, window=3), 1600)
