from file_util import read_lines
from print_aoc import finish_task1, finish_task2
from typing import Callable


def count_amount_of_ones(nums: list[str] | set[str], number_len=12) -> list[int]:
    return [sum(num[i] == "1" for num in nums) for i in range(number_len)]


def task1(lines: list[str], number_len=12) -> int:
    amount_of_ones = count_amount_of_ones(lines, number_len)
    gamma = sum(2 ** (number_len - digit_index - 1) * (amount_of_ones[digit_index] > len(lines) / 2)
                for digit_index in range(number_len))
    epsilon = (2 ** number_len + ~gamma)
    return gamma * epsilon


def to_decimal(num: str) -> int:
    return int(num, 2)


def calc_rating(ls: list[str], comparator: Callable[[float, float], bool], number_len=12) -> int:
    numbers_left = set(ls)
    for i in range(number_len):
        amount_of_ones = count_amount_of_ones(numbers_left)
        criteria_bit = int(comparator(len(numbers_left) / 2, amount_of_ones[i]))
        numbers_left -= set(number_left for number_left in numbers_left if int(number_left[i]) != criteria_bit)
        if len(numbers_left) == 1:
            (number_left,) = numbers_left
            return to_decimal(number_left)


def task2(lines: list[str], number_len=12) -> int:
    return calc_rating(lines, float.__le__, number_len) * calc_rating(lines, float.__gt__, number_len)


if __name__ == '__main__':
    lines = read_lines()
    number_len = len(lines[0])
    finish_task1(3, task1(lines, number_len), 1307354)
    finish_task2(3, task2(lines, number_len), 482500)
