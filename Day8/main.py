from file_util import read_lines
import numpy as np


def parse(lines: list[str]) -> tuple[[list[list[set]]], [list[list[set]]]]:
    output_values = [line.split(" | ")[1] for line in lines]
    output_values = [[set(y) for y in x.split(" ")] for x in output_values]
    patterns = [line.split(" | ")[0] for line in lines]
    patterns = [[set(y) for y in x.split(" ")] for x in patterns]
    return patterns, output_values


def task1(parsed_data: tuple[[list[list[set]]], [list[list[set]]]]) -> int:
    patterns, output_values = parsed_data
    return np.sum([1 for output_value in output_values for value in output_value if len(value) in [2, 3, 4, 7]])


def task2(parsed_data: tuple[[list[list[set]]], [list[list[set]]]]) -> int:
    result = 0
    patterns, output_values = parsed_data
    for pattern, output_value in zip(patterns, output_values):
        # First get 1, 4, 7 and 8
        len_to_pattern = {len(x): x for x in pattern}
        one = len_to_pattern[2]
        four = len_to_pattern[4]
        seven = len_to_pattern[3]
        out_string = ""
        for output in output_value:
            out_string += determine_number(output, one, four, seven)
        result += int(out_string)
    return result


def determine_number(output: str, one: str, four: str, seven: str) -> str:
    output_length = len(output)
    return "1" if output_length == 2 else \
        "7" if output_length == 3 else \
        "4" if output_length == 4 else \
        "8" if output_length == 7 else \
        "2" if output_length == 5 and len(output & four) == 2 else \
        "3" if output_length == 5 and len(output & seven) == 3 else \
        "5" if output_length == 5 and len(output & four) == 3 and len(output & one) == 1 else \
        "9" if output_length == 6 and len(output & four) == 4 else \
        "6" if output_length == 6 and len(output & four) == 3 and len(output & one) == 1 else \
        "0" if output_length == 6 and len(output & four) == 3 and len(output & one) == 2 else ""


if __name__ == "__main__":
    parsed = parse(read_lines())
    print(task1(parsed))
    print(task2(parsed))
