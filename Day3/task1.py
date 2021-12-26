from file_util import read_lines
from print_aoc import finish_task1
from functools import reduce


def gamma_rate(lines: list[str], number_len=12) -> str:
    params = [(index, lines) for index in range(number_len)]
    return reduce(gamma_rate_it, params, "")


def gamma_rate_it(rate: str, params: tuple[int, list[str]]):
    i, lines = params
    return rate + ('1' if is_gamma_bit(i, lines) else '0')


def is_gamma_bit(index: int, lines: list[str]) -> bool:
    params = [(line, index) for line in lines]
    ones, zeroes = reduce(increase_ones_or_zeroes, params, (0, 0))
    return ones > zeroes


def increase_ones_or_zeroes(acc: tuple[int, int], params: tuple[list[str], int]) -> tuple[int, int]:
    line, index = params
    ones, zeroes = acc
    return (ones + 1, zeroes) if line[index] == '1' else (ones, zeroes + 1)


def epsilon_rate(gamma_bin: str) -> str:
    return reduce(lambda acc, num: acc + ('0' if num == '1' else '1'), gamma_bin, "")


def to_decimal(num: str) -> int:
    return int(num, 2)


if __name__ == '__main__':
    lines = read_lines()
    gamma_bin = gamma_rate(lines)
    epsilon_bin = epsilon_rate(gamma_bin)
    finish_task1(3, to_decimal(gamma_bin) * to_decimal(epsilon_bin), 1307354)
