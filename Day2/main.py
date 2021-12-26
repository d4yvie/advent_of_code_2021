from file_util import read_lines
from move import Move
from functools import reduce
from print_aoc import finish_task1, finish_task2


def parse_line(line: str) -> tuple[Move, int]:
    move, severity = line.split(" ")
    return Move(move), int(severity)


calculator_1 = {Move.FORWARD: lambda x, y, severity: (x + severity, y),
                Move.UP: lambda x, y, severity: (x, y - severity),
                Move.DOWN: lambda x, y, severity: (x, y + severity)}


def calc_position_1(coords: tuple[int, int], line: str) -> tuple[int, int]:
    x, y = coords
    move, severity = parse_line(line)
    return calculator_1[move](x, y, severity)


calculator_2 = {Move.FORWARD: lambda x, y, aim, severity: (x + severity, y + aim * severity, aim),
                Move.UP: lambda x, y, aim, severity: (x, y, aim - severity),
                Move.DOWN: lambda x, y, aim, severity: (x, y, aim + severity)}


def calc_position_2(result: tuple[int, int, int], line: str) -> tuple[int, int, int]:
    x, y, aim = result
    move, severity = parse_line(line)
    return calculator_2[move](x, y, aim, severity)


if __name__ == '__main__':
    lines = read_lines()
    x, y = reduce(calc_position_1, lines, (0, 0))
    finish_task1(2, x * y, 1507611)
    x, y, aim = reduce(calc_position_2, lines, (0, 0, 0))
    finish_task2(2, x * y, 1880593125)
