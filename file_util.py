from functools import reduce
import numpy as np


def read_all(file_name="measurements") -> str:
    with open(file_name) as f:
        return reduce(lambda a, b: a + b, f, "")


def read_lines(file_name="measurements") -> list[str]:
    with open(file_name) as f:
        return [line.strip() for line in f]


def read_first_line(file_name="measurements") -> str:
    return read_lines(file_name)[0]


def line_to_integers(line: str) -> list[int]:
    return list(map(int, line.split(",")))


def read_first_line_as_integers(file_name="measurements") -> list[int]:
    return line_to_integers(read_first_line(file_name))


def read_line_seperated_data_sets(file_name="measurements") -> list[str]:
    with open(file_name) as f:
        return f.read().rstrip().split('\n\n')


def read_lines_as_int(file_name="measurements") -> list[list[int]]:
    lines = read_lines(file_name)
    return [[int(char) for char in x] for x in lines]


def read_lines_as_np_matrix(file_name="measurements") -> np.ndarray:
    lines = read_lines(file_name)
    return np.array([[float(char) for char in line] for line in lines])
