from file_util import read_lines_as_np_matrix
from typing import Iterator
from functools import reduce
from print_aoc import print_task1, print_task2
import numpy as np


def create_adjacent_indices(matrix: np.ndarray, x: int, y: int) -> Iterator[tuple[int, int]]:
    for x_offset in -1, 0, 1:
        for y_offset in -1, 0, 1:
            x_new = x + x_offset
            y_new = y + y_offset
            if x == x_new and y == y_new:
                continue
            if (0 <= x_new < matrix.shape[0]) and (0 <= y_new < matrix.shape[1]):
                yield x_new, y_new


def do_step(data: tuple[np.ndarray, int], step_number: int) -> tuple[np.ndarray, int]:
    matrix = data[0].copy()
    matrix += 1
    while (matrix > 9).any():
        for x, y in np.ndindex(*matrix.shape):
            if matrix[x, y] > 9:
                matrix[x, y] = np.nan
                for x_adjacent, y_adjacent in create_adjacent_indices(matrix, x, y):
                    matrix[x_adjacent, y_adjacent] += 1
    number_of_flashes = np.isnan(matrix).sum()
    matrix = np.nan_to_num(matrix)
    return matrix, number_of_flashes + data[1]


def do_steps(matrix: np.ndarray, number_of_steps=100) -> int:
    return reduce(do_step, range(number_of_steps), (matrix, 0))[1]


def first_time_every_octopus_flashes(matrix: np.ndarray) -> int:
    step = 0
    while True:
        if matrix.sum() == 0:
            return step
        matrix, number_of_flashes = do_step((matrix, 0), 0)
        step += 1


if __name__ == "__main__":
    matrix = read_lines_as_np_matrix()
    print_task1(10, do_steps(matrix))
    print_task2(10, first_time_every_octopus_flashes(matrix))

