from task1 import to_decimal
from file_util import read_lines


def calc_oxygen_rating(lines: list[str]) -> int:
    oxygen_rating = lines
    for i in range(len(lines[0])):
        if len(oxygen_rating) == 1:
            return to_decimal(oxygen_rating[0])
        oxygen_rating = filter_oxygen(i, oxygen_rating)
    return to_decimal(oxygen_rating[0])


def filter_oxygen(i: int, lines: list[str]) -> list[str]:
    filtered = []
    for num in lines:
        if not counter(i, lines) and num[i] == '0':
            filtered.append(num)
        elif counter(i, lines) and num[i] == '1':
            filtered.append(num)
    return filtered


def calc_co2_scrubber_rating(lines: list[str]) -> int:
    scrubber_rating = lines
    for i in range(len(lines[0])):
        if len(scrubber_rating) == 1:
            return to_decimal(scrubber_rating[0])
        scrubber_rating = filter_co2(i, scrubber_rating)
    return to_decimal(scrubber_rating[0])


def filter_co2(i: int, lines: list[str]) -> list[str]:
    filtered = []
    for num in lines:
        if not counter(i, lines) and num[i] == '1':
            filtered.append(num)
        elif counter(i, lines) and num[i] == '0':
            filtered.append(num)
    return filtered


def counter(i: int, lines: list[str]) -> bool:
    count_1 = 0
    count_0 = 0
    for bit in lines:
        if bit[i] == '1':
            count_1 += 1
        else:
            count_0 += 1
    return count_1 > count_0 or count_1 == count_0


if __name__ == '__main__':
    lines = read_lines()
    print(calc_oxygen_rating(lines) * calc_co2_scrubber_rating(lines))
