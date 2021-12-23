from file_util import read_lines
from scipy.signal import convolve2d
from print_aoc import finish_task1, finish_task2
from functools import reduce
import numpy as np


EnhanceParameters = tuple[np.array, np.array, np.array]


def enhance_n_times(params: EnhanceParameters, times=2) -> EnhanceParameters:
    return reduce(enhance, range(times), params)


def enhance(params: EnhanceParameters, i: int) -> EnhanceParameters:
    grid, enhancement, kernel = params
    return enhancement[convolve2d(grid, kernel, fillvalue=i % 2)], enhancement, kernel


if __name__ == '__main__':
    lines = read_lines()
    enhancement = np.array(list(lines[0])) == "#"
    grid = np.array(list(map(list, lines[2:]))) == "#"
    kernel = 2 ** np.arange(9).reshape((3, 3))
    grid, enhancement, kernel = enhance_n_times((grid, enhancement, kernel), 2)
    finish_task1(20, grid.sum(), 5306)
    grid, enhancement, kernel = enhance_n_times((grid, enhancement, kernel), 48)
    finish_task2(20, grid.sum(), 17497)
